

# Import Dependencies

import csv
import os

# add variable for file load
file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize total vote counter
total_votes = 0
#candidate options and votes
candidate_options = []
candidate_votes = {}

#Challenge County Options and county votes
county_names = []
county_votes = {}


#track the winning candidate vote count and %
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#challenges track the largest county voter turnouts and %
largest_county_turnout = ""
largest_county_votes = 0

#open and read csv, convert into lists of dict
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # read the header
    header=next(reader)
    #print(header)

    for row in reader:
        total_votes = total_votes +1

        #get candidate name
        candidate_name = row[2]
        #get county_name
        county_name = row[1]

        #If candidate does not match any existing name add it to list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        #Add a vote to candidate count
        candidate_votes[candidate_name] +=1

        #challenge county
        if county_name not in county_names:

         #challenge add to list in the runnning
            county_names.append(county_name)

            #tracking candidate voter count
            county_votes[county_name] = 0

        county_votes[county_name] +=1
#Save result to txt
with open (file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"\n=================\n"
        f"Total Votes: {total_votes:,}"
        f"\n=================\n\n"
        f"County Votes:\n"
    )
    print(election_results, end="")
    txt_file.write(election_results)

    #challenge
    for county in county_votes:
        #get the votes
        county_vote = county_votes[county]
        county_percent = int(county_vote) / int(total_votes) * 100
        county_results = (
            f"{county}: {county_percent:.1f}% ({county_vote:,})\n"
        )
        print(county_results, end="")
        txt_file.write(county_results)


        #determine winner
        if(county_vote > largest_county_votes):
            largest_county_votes = county_vote
            largest_county_turnout = county
    largest_county_turnout = (
        f"\n============================\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"\n=======================\n"
    )
    print(largest_county_turnout)
    txt_file.write(largest_county_turnout)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = int(votes) / int(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
        )

        print(candidate_results)
        txt_file.write(candidate_results)

        #determine winner
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"=============================\n"
        f"winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,} DANG THAT'S A LOTTA VOTES\n"
        f"winning Percentage: {winning_percentage:.1f}%\n"
        f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    )
    print(winning_candidate_summary)

    #SAVE
    txt_file.write(winning_candidate_summary)

