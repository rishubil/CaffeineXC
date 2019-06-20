#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import sounddevice as sd
import numpy  # Make sure NumPy is loaded before it is used in the callback


def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata


if __name__ == "__main__":
    input_index = -1
    output_index = -1
    input_device = None
    output_device = None
    for i, device in enumerate(sd.query_devices()):
        if "Xbox" in device["name"] and device["hostapi"] == 0:
            if device["max_input_channels"] > 0:
                input_index = i
                input_device = device
            elif device["max_output_channels"] > 0:
                output_index = i
                output_device = device

    if input_index == -1 or output_index == -1:
        print("Cannot found Xbox device.")
        print("Press Return to quit.")
        input()
        sys.exit(-1)

    print(f"Input: {input_device['name']}")
    print(f"Output: {output_device['name']}")

    try:
        with sd.Stream(
            device=(input_index, output_index),
            samplerate=output_device["default_samplerate"],
            channels=output_device["max_output_channels"],
            callback=callback,
        ):
            print("Press Return to quit.")
            input()
            sys.exit(0)
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    except Exception as e:
        print(type(e).__name__ + ": " + str(e))

