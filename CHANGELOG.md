# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Add texture loading in the world.
- Add ability to rotate texture.

### Changed

- Update `python` from 3.8 to 3.9.
- Update `isort` from 5.5.4 to 5.6.4.
- Update `colorlog` from 4.4.0 to 4.6.2.
- Update `pygame` from 2.0.0dev12 to 2.0.1.
- Update `pyinstaller` from 4.0 to 4.1.


### Deprecated
### Removed
### Fixed
### Security


## [0.3.0] - 2020.12.20


### Added

- Add `Logger` which can write to terminal and to class.
- Add `Camera` that moves around with player.
- Add option to limit camera scrolling to map size.
- Add `Player` animated sprite.
- Add inertia to the `Player`.
- Add fullscreen mode.

### Changed

- Change player movement to be smooth.

### Deprecated
### Removed
### Fixed
### Security


## [0.2.0] - 2020.10.09

### Added

- Add `Game` class.
- Add `Player` class.
- Add generic `Block` class.
- Add player movement.
- Add player with block collision.

### Fixed

- Fix `pyproject.toml` for building wheels.


## [0.1.0] - 2020-10-06

### Added

- Add script to initialize virtual environment.
- Add `poetry` as a package manager.
- Add `pygame` package.
- Add `black` and `isort` linter packages.
- Add `pyinstaller` to build executables.
