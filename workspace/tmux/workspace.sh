#!/bin/bash

#init session object
echo "Assign sessin: {$USER}"
SESSION=$USER

#build tmux env
tmux new-session -d -s $SESSION
tmux new-window -t $SESSION -n "WORKSPACE"
tmux split-window -v

tmux select-pane -t 0
tmux resize-pane -D 20
tmux send-keys "vim" C-m
sleep 0.3

tmux select-pane -t 1
tmux resize-pane -D 20
tmux send-keys "ls -la" C-m
sleep 0.3

tmux select-pane -t 0

tmux attach-session -t $SESSION 
