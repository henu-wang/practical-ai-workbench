## How to reduce an image's file size

Choose a PNG, JPEG, or WebP image, select JPEG or WebP output, and adjust the quality slider. Generate the result and inspect its actual file size. Lower quality can reduce the download size, but it can also introduce visible blur or blocky edges.

If the image is larger than you need, set a maximum width or height as well. Reducing unnecessary dimensions often helps more than repeatedly lowering quality. The tool keeps the image's proportions and does not enlarge smaller images.

## Try the sample image

Download [sample-image.png](../samples/sample-image.png), a fictional example measuring 1200 × 800 pixels.

1. Choose the sample as your input.
2. Set maximum width to `600` and maximum height to `400`.
3. Select JPEG output and generate the image.
4. Check that the result is 600 × 400 pixels, then compare its reported byte size with the original.
5. Adjust quality and generate again if the result is too large or its appearance is poor.

The dimension result is predictable for this sample. Its exact byte size depends on the format, quality setting, and browser encoder, so the example does not promise a particular download size.

## Can I compress an image to 100 KB?

Use the displayed output size to check your target; this tool does not guarantee an exact 100 KB result. If a form rejects the file, lower quality or dimensions, generate again, and compare the actual bytes with the form's limit. Keep enough detail for the intended use.

An image that is already efficiently compressed may produce an output that is larger. In that case, keep the original if it already meets your requirements. File-size reduction is a result to verify, not a promise attached to the word “compress.”

## Choose a format and check the image

JPEG uses a white background where the input is transparent. If the background matters, try WebP and inspect the downloaded result in the application that will receive it. Confirm that the receiving service accepts your chosen format.

View the output at its intended display size. Look closely at text, fine lines, faces, and edges. Do not choose a tiny result that makes the important content unreadable.

For folder-sized jobs, [Sharp on TokRepo](https://tokrepo.com/en/workflows/sharp-high-performance-image-processing-node-js-f5801cab) is an optional batch-processing asset. This browser tool uses browser image processing rather than Sharp; the asset is a next step for an automated workflow with explicit size and quality checks.
