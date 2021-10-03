.PHONY: build

build:
	sam build

deploy-infra:
	sam build && aws-vault exec crc --no-session -- sam deploy

deploy-site:
	aws-vault exec crc --no-session -- aws s3 sync ./resume-site s3://myawsbucket-resume-page

invoke-put:
	sam build && aws-vault exec crc --no-session -- sam local invoke PutFunction

invoke-get:
	sam build && aws-vault exec crc --no-session -- sam local invoke GetFunction