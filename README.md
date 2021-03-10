# 𝖙𝖍𝖊 𝖆𝖗𝖙 𝖔𝖋 𝖔𝖗𝖉𝖊𝖗

Game about order and chaos ⚖️

You can use both Windows and Linux to play the game.
macOS is not currently supported, although if enough evidence of its necessity is provided, support can be added.
Mobile platforms are not yet supported.

More info later!


## Getting started

You can use both Windows and Linux to build and play the game. macOS is not currently supported.

### Linux
Before buidling the game, you need to initialize development environment. In order to do that, run:

```bash
make init
```

Then you can build your binary by running.

```bash
make build
```

It will create a folder `$PWD/dist/linux/tao_linux_$VERSION_build$DATE$TIME`, which will contain the binary and neccessary files for it to run.

### Windows
Before buidling the game, you need to initialize development environment. In order to do that, run:

```powershell
.\scripts\windows\init.ps1
```

Then you can build your binary by running.

```powershell
.\scripts\windows\build.ps1
```

It will create a folder `$PWD/dist/windows/tao_win_$VERSION_build$DATE$TIME`, which will contain the binary and neccessary files for it to run.


## Development

Development should be pretty much the same on both platforms.

### Windows
Initialization should have created a Python virtual environment, that you can enter by typing:

```powershell
.\.env\Scripts\Activate.ps1
```

Then you can work on the code.

Before commiting, you need to make sure the codestyle is compliant to the standards; for that type:

```powershell
.\scripts\windows\lint.ps1
```

It will sort imports and lint the code using `black`.

### Linux
Initialization should have created a Python virtual environment, that you can enter by typing:

```bash
source .env/bin/activate
```

Then you can work on the code.

Before commiting, you need to make sure the codestyle is compliant to the standards; for that type:

```bash
make lint
```

It will sort imports and lint the code using `black`.
