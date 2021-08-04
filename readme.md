#### Spring Boot Application Monitor

This script checks the health status of a Spring Boot application.

#### Instructions

```bash
$ docker build -t application-monitor .
$ docker run --rm --env-file env_settings.ini (--env <key>=<value>) application-monitor
```
