A [yt-dlp](https://github.com/yt-dlp/yt-dlp) postprocessor [plugin](https://github.com/yt-dlp/yt-dlp#plugins) for [DeArrow](https://dearrow.ajay.app/).

Will modify the title variable to the first return from DeArrow, if any. Does not change on a null response. The original title should be useable with %(original_title)s

## Installation

Requires yt-dlp `2023.01.01` or above.

You can install this package with pip:
```
python3 -m pip install -U https://github.com/QuantumWarpCode/yt-dlp-dearrow/archive/master.zip
```

See [yt-dlp installing plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins) for the many other ways this plugin package can be installed.

## Usage

Pass `--use-postprocessor DeArrow:when=pre_process` to activate the PostProcessor

Pass `--use-postprocessor "DeArrow:when=pre_process;SelectTitle=True"` if you want to choose from the available DeArrow titles

## Credits

Many thanks to [Chris C.](https://github.com/topher-nullset) and the RYD plugin for some code.

Uses SponsorBlock(DeArrow) data licensed used under CC BY-NC-SA 4.0 from https://sponsor.ajay.app/.
