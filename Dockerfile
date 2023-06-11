FROM python:latest
WORKDIR /home/root
#bind output volume here
RUN mkdir -p working/output
COPY Docker/dependencies/ working/
WORKDIR /home/root/working
#bind github workspace here
RUN mkdir repo/
WORKDIR /home/root/working/repo

#find and checkout repo
#WORKDIR /home/root/repo
#RUN readme="$(find -type f -maxdepth 2 -iname "readme.md")"
#RUN repoPath="${readme:0:-10}"
#WORKDIR ${repoPath}
#previously hard coded main, should now get name of branch being pulled to
#RUN git checkout main

#find file paths of changed files for python script
#branch name hard coded again
#RUN git diff --name-only --stat=10000 --output=/home/root/working/changed-files-paths.txt main^ main


ENTRYPOINT ["./entrypoint.sh"]


#run inclusive-naming-checker.py
#WORKDIR /root/working
#RUN python inclusive-naming-checker.py

