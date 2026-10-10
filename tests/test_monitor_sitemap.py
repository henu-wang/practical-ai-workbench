"""An unreadable sitemap must not become a false missing-page diagnosis."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    "monitor_public", Path(__file__).resolve().parents[1] / "scripts/monitor_public.py")
monitor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(monitor)


class SitemapObservation(unittest.TestCase):
    def run_monitor(self, sitemap_body, sitemap_status=200):
        base = "https://editorial.example.test/project/"
        recipe = base + "workflows/example/"

        def response(url, timeout=20, max_bytes=2048):
            status, error = 200, None
            if url == base + "sitemap.xml":
                body, status = sitemap_body, sitemap_status
                if status is None:
                    error = {"type": "RemoteDisconnected", "message": "Test connection failure"}
            elif url.endswith("robots.txt"):
                body, status = b"missing", 404
            elif "/templates/" in url:
                body = b"Original fixture template"
            else:
                body = (f'<html><head><link rel="canonical" href="{url}"></head>'
                        f'<body><a href="{base}templates/example.md">Template</a></body></html>').encode()
            return {"url": url, "final_url": url if status else None,
                    "started_at": "2026-10-09T00:00:00+00:00",
                    "checked_at": "2026-10-09T00:00:00+00:00",
                    "http_status": status, "headers": {"Content-Type": "text/plain"},
                    "x_robots_tag": [], "body_truncated": False,
                    "body_bytes_read": len(body), "_body": body, "error": error}

        with tempfile.TemporaryDirectory() as directory:
            manifest, output = Path(directory) / "manifest.json", Path(directory) / "receipt.json"
            manifest.write_text(json.dumps({"site_url": base, "recipes": [{"slug": "example"}]}))
            with patch.object(monitor, "fetch", response), contextlib.redirect_stdout(io.StringIO()):
                code = monitor.main(["--manifest", str(manifest), "--output", str(output)])
            return code, json.loads(output.read_text()), base, recipe

    def test_connection_failure_and_invalid_xml_leave_membership_unknown(self):
        for body, status in [(b"", None), (b"<broken", 200)]:
            with self.subTest(status=status):
                code, receipt, _, _ = self.run_monitor(body, status)
                self.assertEqual(code, 1)
                self.assertIsNotNone(receipt["sitemap"]["error"])
                for page in [receipt["home"], *receipt["recipes"].values()]:
                    self.assertIsNone(page["in_sitemap"])
                    self.assertNotIn("page_missing_from_sitemap", page["issues"])
                self.assertIsNone(receipt["search_observation"]["gsc_clicks"])

    def test_valid_sitemap_omission_is_a_missing_page(self):
        body = b'<urlset><url><loc>https://editorial.example.test/project/</loc></url></urlset>'
        code, receipt, _, _ = self.run_monitor(body)
        self.assertEqual(code, 1)
        page = receipt["recipes"]["example"]
        self.assertIs(page["in_sitemap"], False)
        self.assertIn("page_missing_from_sitemap", page["issues"])

    def test_valid_sitemap_with_both_pages_passes(self):
        body = (b'<urlset><url><loc>https://editorial.example.test/project/</loc></url>'
                b'<url><loc>https://editorial.example.test/project/workflows/example/</loc></url></urlset>')
        code, receipt, _, _ = self.run_monitor(body)
        self.assertEqual(code, 0)
        self.assertIs(receipt["recipes"]["example"]["in_sitemap"], True)
        self.assertEqual(receipt["search_observation"]["indexed"], "unknown")


if __name__ == "__main__":
    unittest.main()
