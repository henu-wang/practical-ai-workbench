## Turn a recording into a checked transcript

To transcribe an audio file, use speech recognition to produce a draft, then listen back to check names, numbers, and uncertain passages. This recipe combines Whisper for the transcript with FFmpeg for preparing audio from a recording or video. It produces a text file you can edit; it is not an audio-upload service.

**Start with [the Whisper asset on TokRepo](https://tokrepo.com/en/workflows/whisper-openai-speech-text-eb0f9dd6?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=transcribe-audio-to-text)** for the reusable usage material and its supported setup. The [FFmpeg asset](https://tokrepo.com/en/workflows/ffmpeg-universal-multimedia-processing-toolkit-353248b1?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=transcribe-audio-to-text) supplies the complementary media-preparation steps. Adding either asset to an agent's context does not install the underlying software.

| Asset | Job in this recipe | Handoff |
| --- | --- | --- |
| Whisper — primary | Recognize speech and write a transcript | Audio file → draft text |
| FFmpeg — secondary | Extract or prepare a readable audio file | Recording/video → audio for Whisper |

## Get the task package

Download the [transcription checklist](../../templates/transcribe-audio-to-text/review-checklist.md) and [fictional transcript example](../../templates/transcribe-audio-to-text/fictional-transcript.md). The example demonstrates editing and uncertainty labels; it is not a transcript generated from a provided audio fixture.

Before starting, choose whether you need a close transcript or edited reading copy. A close transcript retains the spoken wording; an edited copy can remove repetition but should be labeled accordingly. Keep both when you need an audit trail.

## Prepare and transcribe a short file first

Install the Whisper Python package and system FFmpeg following the asset's upstream instructions. Check that `ffmpeg` is available in your terminal. The first model use can download weights, and recognition takes local compute; there is no guaranteed completion time.

For a video, this example extracts its audio into a mono WAV file:

```bash
ffmpeg -i recording.mp4 -vn -ac 1 -ar 16000 recording.wav
```

Then transcribe the WAV. This example chooses an English-only model and plain text output:

```bash
whisper recording.wav --model base.en --language en --task transcribe --output_format txt --output_dir transcripts
```

Check for `transcripts/recording.txt`. If you already have a supported audio file, try it directly instead of creating an unnecessary conversion. Start with a short excerpt so you can discover setup and recognition problems before processing a long recording.

These commands are source-checked examples; this page does not claim a measured recognition result on your recording. For another language, choose the appropriate multilingual model and language setting rather than an `.en` model.

## Check the output against the recording

Listen to the opening, ending, and each passage containing an important claim. Check every proper name, quantity, date, and commitment. Mark an uncertain phrase as `[unclear — check 00:42]` instead of silently guessing. The checklist has separate fields for the original draft, corrections, and reviewer.

For the fictional example, the useful final output preserves “draft,” distinguishes Friday's proposal from a confirmed deadline, and leaves an unclear product name unresolved. Correct grammar should not change what the speaker committed to.

If the text includes speech that was not actually audible, remove or flag it after listening. Speech recognition can make plausible mistakes, especially with silence, overlapping voices, or poor recordings. A readable transcript is not proof of accuracy.

## Common questions

**Is this free transcription?** The local open source Whisper route does not require a paid transcription API. Your computer's storage, compute, installation effort, and review time still matter. This page does not offer unlimited hosted transcription.

**Will it identify speakers?** This recipe does not provide reliable automatic speaker identification. Add speaker labels only when you can support them from the recording; otherwise use an unknown label.

**Can I use the result as subtitles?** Text alone does not contain subtitle timing. Whisper has subtitle-output options, but timing and line breaks need their own check. Choose the output format for your actual task.

Once the small-file test works, keep the [Whisper asset](https://tokrepo.com/en/workflows/whisper-openai-speech-text-eb0f9dd6?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=transcribe-audio-to-text) with your agent or workflow so the setup, format choices, and review steps are reusable. See the [official Whisper instructions](https://github.com/openai/whisper) and [FFmpeg documentation](https://ffmpeg.org/ffmpeg.html) for the underlying tools.
