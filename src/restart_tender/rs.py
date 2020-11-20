from subprocess import Popen, PIPE
from time import sleep


# windows task scheduler invokes this script every 12 hours +- 5 minutes
# todo: make a loop in a different thread so we can use stdin on the server console


def main():
        with Popen("LaunchServer.bat", stdin=PIPE) as proc:
            sleep(300)
            
            proc.communicate(
                bytes(
                    "/say Server will restart in 12 hours".encode("utf-8")
                )
            )            
            sleep(21600)

            proc.communicate(
                bytes(
                    "/say Server will restart in 6 hours".encode("utf-8")
                )
            )
            sleep(10800)

            proc.communicate(
                bytes(
                    "/say Server will restart in 3 hours".encode("utf-8")
                )
            )
            sleep(7200)
        
            proc.communicate(
                bytes(
                    "/say Server will restart in 1 hour".encode("utf-8")
                )
            )
            sleep(1800)

            proc.communicate(
                bytes(
                    "/say Server will restart in 30 minutes".encode("utf-8")
                )
            )
            sleep(1200)

            proc.communicate(
                bytes(
                    "/say Server will restart in 10 minutes".encode("utf-8")
                )
            )
            sleep(300)

            proc.communicate(
                bytes(
                    "/say Server will restart in 5 minutes".encode("utf-8")
                )
            )
            sleep(240)

            proc.communicate(
                bytes(
                    "/say Server will restart in 1 minute".encode("utf-8")
                )
            )
            sleep(30)

            proc.communicate(
                bytes(
                    "/say Server will restart in 30 seconds".encode("utf-8")
                )
            )
            sleep(20)

            proc.communicate(
                bytes(
                    "/say Server will restart in 10 seconds".encode("utf-8")
                )
            )
            sleep(5)

            proc.communicate(
                bytes(
                    "/say Server will restart in 5 seconds".encode("utf-8")
                )
            )
            sleep(5)
            
            proc.communicate(
                bytes(
                    "stop".encode("utf-8")
                )
            )
            sleep(5)
            proc.communicate(
                bytes(
                    "exit".encode("utf-8")
                )
            )


if __name__ == "__main__":
    main()
