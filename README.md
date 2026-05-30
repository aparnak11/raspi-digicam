# Raspberry Pi Digicam

A custom handheld digital camera built with a Raspberry Pi, touchscreen interface, and Python. The project combines embedded software, camera integration, user interface design, networking, and hardware prototyping into a portable photography device.

## Features

* Live camera preview
* Touchscreen user interface
* Photo capture and storage
* Gallery with photo browsing
* Photo deletion and recovery
* Recently Deleted folder with restore functionality
* Multiple image filters:

  * Normal
  * Black & White
  * Pink
  * Golden
* QR-code photo sharing
* Local web gallery accessible from iPhone
* Portable hotspot-based photo transfer
* Startup and shutdown splash screens

## Hardware

* Raspberry Pi 4 Model B
* Raspberry Pi Camera Module v1.3
* Waveshare 3.5" Capacitive Touch Display
* 64 GB microSD Card
* Portable USB-C Power Bank (in progress)

## Software

* Python
* Picamera2
* Pillow (PIL)
* qrcode
* NetworkManager (nmcli)
* Custom touchscreen and display drivers

## Project Structure

```text
app.py                  # Application entry point
controller.py           # Application state machine
camera.py               # Camera interface
gallery.py              # Photo management
filters.py              # Image filters
touch.py                # Touchscreen handling
display.py              # LCD display interface
share_server.py         # Local photo sharing server

ui/
├── camera_screen.py
├── gallery_screen.py
├── share_screen.py
├── splash_screen.py
└── common.py

photos/
recently_deleted/
vendor/
assets/
```

## Current Status

### Software

* [x] Camera integration
* [x] Live preview
* [x] Photo capture
* [x] Touchscreen UI
* [x] Gallery navigation
* [x] Image filters
* [x] Recently deleted recovery system
* [x] QR photo sharing
* [x] Local web gallery
* [x] Modular codebase

### Hardware

* [x] Raspberry Pi assembly
* [x] Camera module integration
* [x] Touchscreen integration
* [ ] Battery integration and runtime testing
* [ ] Custom enclosure design (Siemens NX)
* [ ] Final portable assembly

## Next Steps

* Integrate portable battery power
* Auto-launch camera application on boot
* Hide Linux desktop and boot directly into camera UI
* Design and manufacture enclosure
* Final field testing and optimization
