.PHONY: api

help:
	@echo "  api: compile protobuf files for python"

api:
	python -m grpc_tools.protoc -I./api/email_client_service --python_out=./src --grpc_python_out=./src ./api/email_client_service/email-client-service.proto
	# if [ ! -d "./pkg/api" ]; then mkdir -p "./pkg/api"; else  find "./pkg/api" -type f -delete &&  mkdir -p "./pkg/api"; fi
	# find ./api/email_client_service/*.proto -maxdepth 1 -type f -exec protoc {} --proto_path=./api --go_out=plugins=grpc:$(PROTO_BUILD_DIR) \;
	# find ./api/messaging_service/*.proto -maxdepth 1 -type f -exec protoc {} --proto_path=./api --go_out=plugins=grpc:$(PROTO_BUILD_DIR) \;
