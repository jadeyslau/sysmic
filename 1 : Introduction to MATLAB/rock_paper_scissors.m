function outcome = rock_paper_scissors(n_rounds)

choices = [ "rock" "paper" "scissors" ];
human_score = 0;
ai_score = 0;

disp(["Playing",num2str(n_rounds),"rounds"]);

for i = 1:n_rounds
    disp("Lets play!");
    human_choice = input("Please enter your choice (rock paper or scissors):\n\n","s");
    rand_number = randi(3);
    ai_choice = choices(rand_number);
    disp("vs");
    disp(ai_choice);
    disp(" ");

        if human_choice == "rock" & ai_choice == "rock"
            disp("We chose the same thing...");            
            disp("draw!");
        
        elseif human_choice == "rock" & ai_choice == "scissors"
            disp("Your rock blunts my scissors");
            disp("You WIN !!!");
            human_score = human_score + 1;
        
        elseif human_choice == "rock" & ai_choice == "paper"
            disp("My paper wraps your rock");
            disp("I WIN!!!");
            ai_score = ai_score + 1;

        elseif human_choice == "scissors" & ai_choice == "rock"
            disp("My rock blunts your scissors");
            disp("I WIN!!!");
            ai_score = ai_score + 1;
        
        elseif human_choice == "scissors" & ai_choice == "scissors"
            disp("We chose the same thing...");
            disp("draw!");
        
        elseif human_choice == "scissors" & ai_choice == "paper"
            disp("Your scissors cut my paper");
            disp("You WIN !!!");
            human_score = human_score + 1;
        
        elseif human_choice == "paper" & ai_choice == "rock"
            disp("Your paper wraps my rock");
            disp("You WIN!!!!");
            human_score = human_score + 1;
            
        elseif human_choice == "paper" & ai_choice == "scissors"
            disp("My scissors cut your paper");            
            disp("I WIN!!!");
            ai_score = ai_score + 1;

        elseif human_choice == "paper" & ai_choice == "paper"
            disp("We chose the same thing...");
            disp("draw!");
            
        else
            disp("You cannot spell! My point!");
            ai_score = ai_score + 1;
        end
        disp(" ");
        scores = sprintf("Human: %d   Computer: %d",human_score, ai_score);
        disp(scores);

        if i<n_rounds
            input("-- Press enter to continue --  \n\n\n","s");
end

if ai_score > human_score
    outcome = "the computer won the game";
elseif ai_score < human_score
    outcome = "the human won the game";
else
    outcome = "the game was tied";
    
end
end
