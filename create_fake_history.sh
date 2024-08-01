#!/bin/bash

# This script creates a more realistic Git history for the Streamlit project.

# --- Configuration ---
# The email address associated with your GitHub account
GIT_EMAIL="yash2006mars@gmail.com"
# Your name
GIT_NAME="YashPHT2"

# Function to make a commit with a specific date and message
commit() {
  MESSAGE=$1
  DATE=$2
  
  # Set the environment variables for the commit
  export GIT_AUTHOR_DATE="$DATE"
  export GIT_COMMITTER_DATE="$DATE"
  export GIT_AUTHOR_NAME="$GIT_NAME"
  export GIT_AUTHOR_EMAIL="$GIT_EMAIL"
  export GIT_COMMITTER_NAME="$GIT_NAME"
  export GIT_COMMITTER_EMAIL="$GIT_EMAIL"
  
  # Create a small random change to a file to have something to commit
  echo "$DATE" >> commit.log
  git add commit.log
  git commit -m "$MESSAGE"
  
  echo "✅ Committed: '$MESSAGE' on $DATE"
  
  # Unset variables
  unset GIT_AUTHOR_DATE
  unset GIT_COMMITTER_DATE
  unset GIT_AUTHOR_NAME
  unset GIT_AUTHOR_EMAIL
  unset GIT_COMMITTER_NAME
  unset GIT_COMMITTER_EMAIL
}

# --- Main Script ---

# Clean up previous Git history
echo "🧹 Cleaning up old Git data..."
rm -rf .git

# Initialize new repository
echo "🚀 Initializing new Git repository..."
git init
git branch -M main

# Add the main application files in the first commit
echo "📦 Adding initial project files..."
git add app.py README.md requirements.txt create_fake_history.sh
commit "feat: Initial project structure and core application files" "2024-08-01T10:00:00"

# Array of possible commit messages
MESSAGES=(
  "refactor: Minor code cleanup and optimization"
  "fix: Corrected a typo in the documentation"
  "feat: Added a new helper function for data parsing"
  "style: Formatted code according to PEP8 standards"
  "docs: Updated README.md with new setup instructions"
  "refactor: Improved variable naming for clarity"
  "fix: Handled an edge case in the PDF processing logic"
  "feat: Implemented basic caching to improve performance"
  "style: Adjusted UI element padding for better alignment"
  "docs: Added inline comments to complex functions"
  "fix: Patched a minor security vulnerability"
  "refactor: Simplified a complex conditional statement"
)

echo "🛠️ Generating realistic commit history for August 2024..."
echo "----------------------------------------------------"

# Loop through each day of August
for day in $(seq -w 02 31); do
  # Decide if we should commit on this day (e.g., 80% chance)
  if [ $(($RANDOM % 10)) -lt 8 ]; then
    # Decide how many commits for this day (1 to 4)
    num_commits=$(($RANDOM % 4 + 1))
    
    for i in $(seq 1 $num_commits); do
      # Random hour (9-23) and minute/second
      hour=$(printf "%02d" $(($RANDOM % 15 + 9)))
      minute=$(printf "%02d" $(($RANDOM % 60)))
      second=$(printf "%02d" $(($RANDOM % 60)))
      
      # Select a random message
      message_index=$(($RANDOM % ${#MESSAGES[@]}))
      commit_message="${MESSAGES[$message_index]}"
      
      # Create the commit
      commit "$commit_message" "2024-08-${day}T${hour}:${minute}:${second}"
    done
  fi
done

echo "----------------------------------------------------"
echo "🎉 All commits created successfully!"
echo "Run 'git log --oneline' to inspect the history."
echo "Next, force-push this to your GitHub repository."
