'use strict';
(() => {
  const root = document.querySelector('[data-tool]');
  if (!root) return;
  const kind = root.dataset.tool, W = window.Workbench;
  const $ = id => document.getElementById(id);
  let files = [], resultURL = null;
  const message = (text, error = false) => { $('status').textContent = text; $('status').className = error ? 'status error' : 'status'; };
  function clearResult() {
    if (resultURL) URL.revokeObjectURL(resultURL);
    resultURL = null;
    $('result').hidden = true; $('download').removeAttribute('href');
    $('preview').replaceChildren(); $('result-summary').textContent = '';
  }
  function download(blob, name, summary) {
    clearResult(); resultURL = URL.createObjectURL(blob);
    $('download').href = resultURL; $('download').download = name;
    $('result-summary').textContent = summary; $('result').hidden = false;
    message('Done. Review the result, then download your file.');
  }
  function renderFiles() {
    const list = $('file-list'); if (!list) return;
    list.replaceChildren();
    files.forEach((file, index) => {
      const item = document.createElement('li'), label = document.createElement('span');
      label.textContent = `${index + 1}. ${file.name} (${(file.size / 1024).toFixed(1)} KiB)`; item.append(label);
      if (kind === 'merge-pdf') {
        for (const [label, delta] of [['Move up', -1], ['Move down', 1]]) {
          const button = document.createElement('button'); button.type = 'button'; button.textContent = label;
          button.disabled = index + delta < 0 || index + delta >= files.length;
          button.addEventListener('click', () => {
            [files[index], files[index + delta]] = [files[index + delta], files[index]];
            clearResult(); renderFiles(); message('File order updated.');
          }); item.append(button);
        }
      }
      list.append(item);
    });
  }
  $('files').addEventListener('change', () => {
    files = Array.from($('files').files); clearResult(); renderFiles();
    message(files.length ? `${files.length} file${files.length > 1 ? 's' : ''} selected.` : 'Choose files or try the sample.');
  });
  $('reset').addEventListener('click', () => {
    files = []; $('files').value = ''; if ($('csv-text')) $('csv-text').value = '';
    clearResult(); renderFiles(); message('Cleared. Your files were not uploaded.');
  });
  $('try-sample').addEventListener('click', async () => {
    try {
      clearResult(); message('Loading example files…');
      const names = kind === 'merge-pdf' ? ['source-a.pdf', 'source-b.pdf'] : kind === 'extract-pdf-pages' ? ['source-a.pdf'] : kind.includes('image') ? ['sample-image.png'] : ['data.csv'];
      files = await Promise.all(names.map(async name => {
        const r = await fetch('../samples/' + name); if (!r.ok) throw new Error('Example file could not load.');
        return new File([await r.blob()], name, { type: name.endsWith('.pdf') ? 'application/pdf' : name.endsWith('.png') ? 'image/png' : 'text/csv' });
      }));
      if ($('csv-text')) { $('csv-text').value = await files[0].text(); files = []; }
      if ($('pages')) $('pages').value = '2,1';
      renderFiles(); message('Example ready. Select your options and run the tool.');
    } catch (error) { message(error.message, true); }
  });
  function tablePreview(table) {
    const element = document.createElement('table'), head = document.createElement('thead'), row = document.createElement('tr');
    for (const label of table.headers) { const cell = document.createElement('th'); cell.textContent = label; row.append(cell); }
    head.append(row); element.append(head);
    const body = document.createElement('tbody');
    for (const values of table.rows.slice(0, 8)) {
      const line = document.createElement('tr');
      for (const value of values) { const cell = document.createElement('td'); cell.textContent = value; line.append(cell); }
      body.append(line);
    }
    element.append(body); const wrap = document.createElement('div'); wrap.className = 'table-scroll'; wrap.append(element); $('preview').append(wrap);
  }
  $('run').addEventListener('click', async () => {
    clearResult(); $('run').disabled = true; message('Processing in your browser…');
    try {
      if (kind === 'merge-pdf' || kind === 'extract-pdf-pages') {
        if (!files.length) throw new Error('Choose PDF files or try the sample.');
        if (files.length > 10 || files.reduce((sum, f) => sum + f.size, 0) > 40 * 1024 * 1024) throw new Error('Use at most 10 PDFs and 40 MiB total.');
        if (kind === 'extract-pdf-pages' && files.length !== 1) throw new Error('Choose one PDF to extract pages from.');
        const inputs = await Promise.all(files.map(f => f.arrayBuffer()));
        const output = kind === 'merge-pdf' ? await W.mergePDF(inputs) : await W.extractPDF(inputs[0], $('pages').value);
        const summary = kind === 'merge-pdf' ? `${files.length} files → ${output.pages} pages, ${(output.bytes.length / 1024).toFixed(1)} KiB.` : `Pages ${output.selection.join(', ')} from ${output.sourcePages} source pages → ${output.pages} output pages.`;
        download(new Blob([output.bytes], { type: 'application/pdf' }), kind === 'merge-pdf' ? 'merged.pdf' : 'extracted-pages.pdf', summary);
      } else if (kind.includes('image')) {
        if (files.length !== 1) throw new Error('Choose one image or try the sample.');
        const type = $('format').value;
        const output = await W.convertImage(files[0], { type, quality: Number($('quality').value), maxWidth: Number($('width').value), maxHeight: Number($('height').value) });
        const change = (100 * (1 - output.blob.size / output.inputBytes)).toFixed(1);
        const summary = `${output.originalWidth} × ${output.originalHeight} → ${output.width} × ${output.height} px. ${(output.inputBytes / 1024).toFixed(1)} → ${(output.blob.size / 1024).toFixed(1)} KiB. ${Number(change) >= 0 ? change + '% smaller.' : Math.abs(Number(change)).toFixed(1) + '% larger; try lower quality or dimensions.'}`;
        download(output.blob, type === 'image/webp' ? 'processed.webp' : 'processed.jpg', summary);
        const image = document.createElement('img'); image.src = resultURL; image.alt = `Processed image, ${output.width} by ${output.height} pixels`; image.className = 'image-preview'; $('preview').append(image);
      } else {
        const pasted = $('csv-text').value;
        if (files.length > 1) throw new Error('Choose one CSV file.');
        if (files.length && files[0].size > 10 * 1024 * 1024) throw new Error('Use a CSV smaller than 10 MiB.');
        const text = pasted.trim() ? pasted : files.length ? await files[0].text() : '';
        if (new Blob([text]).size > 10 * 1024 * 1024) throw new Error('Use CSV text smaller than 10 MiB.');
        const parsed = W.parseCSV(text);
        if (kind === 'csv-to-json') {
          const json = W.jsonOutput(parsed);
          download(new Blob([json], { type: 'application/json' }), 'data.json', `${parsed.rows.length} data rows → ${parsed.rows.length} JSON objects. Values remain strings.`);
          const preview = document.createElement('pre'); preview.textContent = W.jsonOutput({ headers: parsed.headers, rows: parsed.rows.slice(0, 8) }); $('preview').append(preview);
        } else {
          const chosen = $('key-column').value.trim();
          let column = -1;
          if (chosen) { column = parsed.headers.indexOf(chosen); if (column === -1) throw new Error('Key column was not found. Enter an exact header name, or leave it blank for all columns.'); }
          const output = W.deduplicate(parsed, { column, keep: $('keep').value, trim: $('trim').checked, ignoreCase: $('ignore-case').checked });
          const safe = $('formula-safe').checked;
          download(new Blob([W.csvOutput(output, safe)], { type: 'text/csv;charset=utf-8' }), 'deduplicated.csv', `${parsed.rows.length} rows → ${output.rows.length}; ${output.removed} duplicates removed.${safe ? ' Spreadsheet formula protection enabled; affected cells receive an apostrophe prefix.' : ''}`);
          tablePreview(output);
        }
      }
    } catch (error) { clearResult(); message(error.message || 'Processing failed. Try a smaller file.', true); }
    finally { $('run').disabled = false; }
  });
  if ($('quality')) $('quality').addEventListener('input', () => { $('quality-value').textContent = Math.round(Number($('quality').value) * 100) + '%'; });
})();
