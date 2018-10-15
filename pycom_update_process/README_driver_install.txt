This document describes the firmware update process for pycoms pysense/pytrack/expansion board. 
At iot-challenge-2018 all boards are labeled with their current firmware version.
Following Pycom documentation on how to upgrade firmware( https://docs.pycom.io/pytrackpysense/installation/firmware ):

prerequisites:
- zadig ( https://zadig.akeo.ie/ ) (program to install the libusbk driver on pycom-board)
- libusbk driver ( https://sourceforge.net/projects/libusbk/files/latest/download )
- latest firmware in .dfu format ( https://docs.pycom.io/pytrackpysense/installation/firmware )

to update pysense/pytrack/expansion3 (from now called [device]):
1. usb-driver for board-pc update communication must be installed on host pc(libusbk)
2. latest board firmware must be installed on edge device (comes as a .dfu file)

Install upgrade driver libusbk on microcontroller(can be skipped if board is already setup on older fimware):

1. open zadig, and device manager. note: libusbK driver must be installed on host pc. 
2. select libusbk in zadig and enable "list all devices"
3. hold button on device (S1 on expansion3) while connecting, until device manager refreshes to show new device. (device is now in bootloader mode for 7 seconds)
4. immediately press "install driver". if zadig prompts "success" go on, else repeat from 1.
5. check that the driver was installed correctly by reconnecting with button pressed and make sure device manager shows a new "libusbk device" NOT "COM device"

Use the dfu-util to upgrade firmware:
1. connect board in bootloader mode as described above (board stays only 7 seconds in bootloader mode. be quick!)
2. run dfu-util-static.exe -D [device]_X.X.X.dfu
3. dfu-util should output something like shown in picture "successful_driver_installation.png"

[device] is now compatible with VSCode extention pymakr and lopy4.