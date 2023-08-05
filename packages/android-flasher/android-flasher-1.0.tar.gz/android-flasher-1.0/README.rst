Flasher
=======

Flasher is a shell script generator which helps you to flash the Android
factory image without removing user data.

You can use it instead of ``flash-all.sh`` or ``flash-all.bat``.

How does it work
~~~~~~~~~~~~~~~~

1. Clone this repository.
2. Copy the ``flasher.py`` file from the repository to the unzipped
   factory image directory.
3. Run ``python flasher.py`` in terminal.
4. Then it will prepare to flash and generate ``flasher.sh``.
5. Now reboot and enter the bootloader.
6. Execute the ``flasher.sh`` script.

License
~~~~~~~

`The MIT License (MIT)`_

Copyright (c) 2015 Minsoo Park

.. _The MIT License (MIT): https://github.com/minsoopark/android-flasher/blob/master/LICENSE