init:
	./scripts/init.sh

lint:
	./scripts/lint.sh

release-windows:
	docker build -t tao-windows-builder .
	docker run -v "/wine/drive_c/src/" tao-windows-builder

	$(eval CONTAINER_ID = $(shell docker ps -alq))
	$(eval DATE = $(shell date +%F-%T))

	mkdir dist/windows/build_${DATE}
	docker cp ${CONTAINER_ID}:/src/dist/tao/ ./dist/windows/build_${DATE}/

release-linux:
	./scripts/release.sh

release: release-windows release-linux
