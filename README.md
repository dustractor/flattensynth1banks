# flattensynth1banks
tiny python script maybe useful for Synth1 users

    python flattensynth1banks.py --source "C:\directory\foo" --target "C:\directory\bar"

Synth1 patches are numbered 001.sy1 through 128.sy1 and organized in banks by folder.  A maximum of 100 folders may be configured (via the OPT button in Synth1) meaning that the internal preset system can hold 12,800 presets.  That's a lot of presets!

I downloaded the roughly 8,600+ [presets shared on KVR](https://www.kvraudio.com/product/synth1-by-daichi-laboratory-ichiro-toda/downloads) and decided I'd rather not have a bunch of banks with empty spots and only a few patches per bank so I made this script to copy all the presets from one folder structure and rename them according to their new position within the hierarchy.
