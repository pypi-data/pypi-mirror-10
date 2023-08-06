# Changelog

## 1.0.0

1. _Active -> _Backend
2. done_message -> done, abort_message -> abort, clear_message -> clear
3. Agent: start -> start_backend, stop -> stop_backend

## 0.1.9

1. -_Active._agent
2. stop agent when backend thread exit
3. fix wrapper return value

## 0.1.8

+ clear_message

## 0.1.7

+ break the thread if handle_message return False

## 0.1.6

+ done_message & abort_message

## 0.1.5

setDaemon(True)
do not force terminate backend thread when stop

## 0.1.4

+ backend thread restart mechanism

## 0.1.3

fix backend & frontend pass args, kwargs to _CallWrapper error

## 0.1.2

handle frontend in main thread & backend in sub thread

## 0.1.1

+ decorator: frontend & backend

## 0.1.0

Initial release.
