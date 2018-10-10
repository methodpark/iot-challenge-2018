Follow Pycom documentation on how to upgrade firmware( https://docs.pycom.io/pytrackpysense/installation/firmware ):

to update pysense/pytrack/expansion3 (from now called [device]):
1. usb-driver for board-pc update communication must be installed (libusB)
2. latest board firmware must be installed (comes as a .dfu file)

Install upgrade driver libusbk (can be skipped if board is already setup on older fimware):

1. open zadig, and device manager. note: libusbK driver must be installed on host PC
2. in zadig enable "list all devices"
3. hold button on device(S1 on expansion3) while connecting, until device manager refreshes to show new device. (device is now in bootloader mode for 7 seconds)
4. immediately press "install driver". if zadig prompts "success" go on, else repeat from 1.
5. check that the driver was installed correctly by reconnecting with button pressed and make sure device manager shows a new "libusbk device" NOT "COM device"

Use the dfu-util to upgrade firmware:
1. connect board in bootloader mode as described above (only 7 seconds remaining to proceed to next step)
2. run dfu-util-static.exe -D [device]_X.X.X.dfu
3. dfu-util should output something like shown in picture "successful_driver_installation.png"

[device] is now compatible with VSCode extention pymakr and lopy4.