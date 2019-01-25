# Face Verify

Upload images to database and compare live video feed to existing images.
This project is to ultimately run as a standalone software for facial verification


- [Face Verify](#face-verify)
  - [Getting Started](#getting-started)
  - [Usage](#usage)
    - [Upload](#upload)
    - [Verification](#verification)
  - [API Documentation](#api-documentation)
  - [Credits](#credits)
  - [Contribution](#contribution)
  - [License (MIT)](#license-mit)
  - [Todo](#todo)

## Getting Started

Setup Virtual environment and install requirements

```bash
    mkvirtualenv face-verify && pip install -r requirements
```

## Usage

Currently only usable as python code or command line

### Upload

To upload an image to the database

```bash
    python main.py upload --name "Firstname Lastname"
```

```python
    from handlers import Uploader

    uploader = Uploader(name="Firstname Lastname")
    uploader.run()
```

### Verification

To run verification on images existing in the database

```bash
    python main.py verify
```

```python
    from handlers import Verifier

    verifiier = Verifier()
    verifier.run()
```

## API Documentation

[Github Pages](https://deven96.github.io/face_verify)

## Credits

- [Dlib](https://dlib.net)
- [Face_recognition](https://face-recognition.readthedocs.io/en/latest/face_recognition.html)
- [OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/)

## Contribution

You are very welcome to modify and use them in your own projects.

Please keep a link to the [original repository](https://github.com/deven96/face_verify). If you have made a fork with substantial modifications that you feel may be useful, then please [open a new issue on GitHub](https://github.com/deven96/face_verify/issues) with a link and short description.

## License (MIT)

This project is opened under the [MIT 2.0 License](LICENSE) which allows very broad use for both academic and commercial purposes.

A few of the images used for demonstration purposes may be under copyright. These images are included under the "fair usage" laws.

## Todo

- Initialize GUI project
- Switch from folder to persistent database handling
- Multiple camera input attachment across local network
- Make into standard python package
- Integrate CI/CD for automatically pushing latest releases to PyPI