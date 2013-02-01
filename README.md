# Denglu Python SDK

## summary

This is not official version of Denglu SDK

It just translate from the official PHP-Version directly to Python

## Usage

Python

	token = request.GET.get('token')
	api = Denglu("50559denaU3C7ytzIQ0jcN2rgAn3j5","848775051pvw176q4tGb1FXhy6MpL3","utf-8")
	userInfo = api.getUserInfoByToken(token)
	
That's all
