## How to resize an image without stretching it

Select a PNG, JPEG, or WebP image and enter maximum width and height. The tool fits the image inside those bounds while preserving its proportions. It does not crop the image, stretch it to fill a box, or enlarge an image that is already smaller.

Choose JPEG or WebP output and generate the download. Quality affects the encoded file and its size; width and height control the maximum pixel dimensions.

## Try an exact 600 × 400 example

Download [sample-image.png](../samples/sample-image.png). This fictional example is 1200 × 800 pixels, so its width and height have the same proportions as 600 × 400.

1. Choose the sample in the tool.
2. Enter `600` for maximum width and `400` for maximum height.
3. Choose an output format and generate the image.
4. Open the download's image properties. The expected dimensions are 600 × 400 pixels.

Now consider a different box: setting maximum width to `640` and maximum height to `480` does not force this sample to become 640 × 480. The image fits within that box; preserving its proportions means the height is less than 480. Small rounding differences can occur because image dimensions use whole pixels.

## Fit inside a box or crop to a box?

Use this tool when a website requires an image no larger than certain dimensions and you want to keep the whole picture. If it requires an exact square profile photo or a fixed-aspect banner, you may need cropping instead. Resizing alone cannot create a different shape without stretching or removing part of the picture.

For example, fitting a landscape photo inside a square leaves it landscape. There is no automatic crop or added border that turns it into a square file.

## Check the downloaded result

Confirm the pixel dimensions in your image viewer, then inspect the important content at the size where it will be displayed. A smaller image can make a screenshot's text difficult to read even when the resizing worked correctly.

Also check the output format and file size. JPEG turns transparent areas white. If preserving a transparent background matters, try WebP and check the receiving application's compatibility. If your goal is primarily a smaller download, see [Compress image](../compress-image/) for quality and byte-size checks.

For a repeated image workflow, [Jimp on TokRepo](https://tokrepo.com/en/workflows/jimp-pure-javascript-image-processing-node-js-0b52787e) is an optional JavaScript processing asset. This page's tool uses browser image processing; Jimp is a separate route for building and checking a batch pipeline.
