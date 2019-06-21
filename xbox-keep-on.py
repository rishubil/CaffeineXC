#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import sounddevice as sd
import numpy  # Make sure NumPy is loaded before it is used in the callback


def callback(outdata, frames, time, status):
    pass


if __name__ == "__main__":
    output_index = -1
    output_device = None
    for i, device in enumerate(sd.query_devices()):
        if (
            "Xbox" in device["name"]
            and device["hostapi"] == 0
            and device["max_output_channels"] > 0
        ):
            output_index = i
            output_device = device
            print(f"Output: {output_device['name']}")
            break
    else:
        print("Cannot found Xbox device.")
        print("Press Return to quit.")
        input()
        sys.exit(-1)

    try:
        with sd.OutputStream(device=output_index, callback=callback):
            print("Press Return to quit.")
            input()
            sys.exit(0)
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    except Exception as e:
        raise e
        print(type(e).__name__ + ": " + str(e))

