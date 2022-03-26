#include <random>
#include <iostream>
#include <string>
#include <chrono>
#include <Windows.h>
#pragma comment(lib, "winmm.lib")


void myFunction(int ehealth, int ghealth, std::string ename, std::string gname, double hdam, double qdam) {
    std::string dead;
    PlaySoundW(L"BIG SHOT.wav", NULL, SND_FILENAME | SND_LOOP | SND_ASYNC);
    for (double x = ghealth, y = ehealth, neadead = (y * .50), trigger = 0; x > 0 && y > 0;) {
        std::random_device dev;
        std::mt19937 rng(dev());
        int move = 0;
        int dam = 0;
        double dedam = 0.0;
        if (y < neadead && trigger == 0) {
            std::uniform_int_distribution<std::mt19937::result_type> dist7(1, 3);
            trigger = dist7(rng);
            double per = 0.0;
            if (trigger == 1) {
                per = per + .05;
            }
            else if (trigger == 2) {
                per = per + .20;
            }
            else {
                per = per + .40;
            }
            std::cout << ename << ": Damn, this harder than i thought! \n" << ename << " used trigger! his attacks are boosted by " << per << "%!\n";
            qdam = (qdam * per) + qdam;
            hdam = (hdam * per) + hdam;
        }
        std::cout << gname << " health : " << x << "   " << ename << " health : " << y << "\n";
        std::cout << "\n1.)Kick\n2.)punch\n3.)Dodge\nEnter your move against " << ename << ": ";
        std::cin >> move;
        if (move > 3 || move < 0) {
            std::cout << "\nYou just sat there!\n";
        }
        else {
            if (move == 1) {
                std::uniform_int_distribution<std::mt19937::result_type> dist6(1, 3);
                int attack = dist6(rng);
                if (attack == 2) {
                    dam = 26;
                }
                else if (attack == 1) {
                    dam = 19;
                }
                else if (attack == 3) {
                    dam = 11;
                }
                std::cout << "\nYou used a kick! it did " << dam << " points of damage!\n";
                y = y - dam;
                std::cout << gname << " health : " << x << "   " << ename << " health : " << y << "\n";
            }
            else if (move == 2) {
                std::uniform_int_distribution<std::mt19937::result_type> dist6(1, 3);
                int attack = dist6(rng);
                if (attack == 2) {
                    dam = 29;
                }
                else if (attack == 1) {
                    dam = 21;
                }
                else if (attack == 3) {
                    dam = 13;
                }
                std::cout << "\nYou used a punch! it did " << dam << " points of damage!\n";
                y = y - dam;
                std::cout << gname << " health : " << x << "   " << ename << " health : " << y << "\n";
            }
            else if (move == 3) {
                std::cout << "\nYou prepared to dodge an attack!\n";
            }
            std::uniform_int_distribution<std::mt19937::result_type> dist5(1, 2);
            int echance = dist5(rng);
            std::string en;
            if (echance == 1) {
                en = "quirk";
            }
            else {
                en = "physical fighting skills";
            }
      
            if (en == "quirk") {
                dedam = dedam + qdam;
            }
            else {
                en = "physical fighting skills";
                dedam = dedam + hdam;
            }
            if (y <= 0) {
                PlaySound(NULL, NULL, SND_ASYNC);
                std::cout << "\nYou Win!\n";
                trigger = 0;
                system("PAUSE");
            }
            else if (move == 3) {
                std::uniform_int_distribution<std::mt19937::result_type> dist5(1, 3);
                int chance = dist5(rng);
                if (chance == 1) {
                    std::cout << "\n" << ename << " used his " << en << "! but you dodged!\nYou gained some health back!\n";
                    x = x + (x * .37);
                }
                else {
                    std::cout << "\n" << ename << " used his " << en << "! you couldn't dodge in time!\n";
                    std::cout << "\n" << ename << " did " << dedam << " points of damage!\n";
                    if (x - dedam <= 0) {
                        dead = "yes";
                    }
                    x = x - dedam;
                }
            }
            else {
                std::cout << "\n" << ename << " used his " << en << "!\n";
                std::cout << "\n" << ename << " did " << dedam << " points of damage!\n";
                if (x - dedam <= 0) {
                    dead = "yes";
                }
                x = x - dedam;
            }
        }

    }
    if (dead == "yes") {
        std::cout << "YOU DIED!\n";
        abort();
    }
}

int main()
{
    int input;
    std::string winner;
    std::string name = "Kid";
    std::string dead;
    int shigaraki = 0;
    int decide = 0;
    int quiet = 0;
    int AM = 0;
    bool tdead = false;
    bool cdead = false;
    bool comcap = false;
    bool dcaptu = false;
    std::cout << "Shigaraki: Hey wake up!\nShigaraki: C'mon you've been out for an hour!\nShigaraki: Wake up " << name << "!\nShigaraki: Your finally awake.\n";
    std::cout << name << ": Where am i?\nShigaraki: during the Deika city incident you fell outta the sky, Twice decide to take you with use when we were going to the hospital.\n";
    std::cout << "\n\n1.)Deika city? Twice? outta the sky???? Your either high or im high\n2.)Damn, drank too much and now im in my hero academia, I at least wanted to land in UA instead!\n3.)I know where i am and who your are, just give me my gear\nEnter your choice:";
    std::cin >> input;
    if (input == 1) {
        std::cout << "Shigaraki:What? you seriously have no memory of what has happened?\nToga:I think he came from another world!\nDabi:And why would you think that?\nToga:He was mumbling something about going to a different world when we found him.\n" << name << ":Thats right! I was sleeping and dreaming about going to a different world, maybe thats why im here!\n";
        decide++;
    }
    else if (input == 2) {
        std::cout << "Shigaraki:You'd want to land in a place like UA??? That's disgusting, this place is way better. Also, what is this my hero academia??\nDabi:Forget about, him talking about UA is enough to conclude that he at least knows what going on\nShigaraki:Yeah your right\n";
        AM++;
    }
    else if (input == 3) {
        std::cout << "Shigaraki:Right to the point then " << name << ", I like that\n" << name << ": My name isn't kid, its ";
        std::cin >> name;
        std::cout << "Shigaraki:Well alright then " << name << ", put on your gear and lets get started, were gonna attack UA before i go through my surgery.\n";
        shigaraki++;
    }
    else {
        std::cout << "(invalid choice, you said nothing instead)";
        std::cout << "\nShigaraki: You seem to have some condition that halts your thinking, dabi, should we kill this guy or let him join the leauge?\nDabi:Let's keep him\nShigaraki:Ok then guess you live today noobie, lets get to UA, we need to begin our attack.\n";
        quiet++;
    }
    if (input != 3 && quiet == 0) {
        std::cout << "Shigaraki:Well then, You gonna join us or what?\n\n1.)Yes\n2.)No\nEnter your choice:";
        std::cin >> input;
        if (input == 2) {
            std::cout << "Shigaraki:Well then die i guess, aint got time for trash like you.\nYOU DIED\n";
            abort();
        }
        else {
            if (input == 1) {
                std::cout << "Shigaraki:Great!, Grab your gear and lets get a move onto UA errrr... Whats your name?\n";
                std::cin >> name;
            }
            else {
                std::cout << "(invalid choice, you said nothing instead)\n";
                std::cout << "Shigaraki: I'll take your silence as a yes, Grab your gear and lets get a move onto UA.";
                quiet++;
            }
        }
    }
    std::cout << "Shigaraki: We've made it to UA! thanks for the ride kurogiri!\nkurogiri:Please help me im literally a corpse :(\nDabi:Shut up, me and shigaraki will deal with top heros like eraser head and cementos as well as hawks since he happens to be visitng UA, twice will fight Deku and Dynamight with an army of clones and toga,spinner, and compress will take care of smaller hero's.\nTwice:Leave it to me!\nSpinner:What about " << name << "?\n" << "Shigaraki:He'll fight the kids at the dorms, since you got no powers you might die but hey that gear we gave you is pretty good and you said on the way here that you know how to fight " << name << ".\n" << name << ":Yeah i can handle it.\n";
    std::cout << "\n\nThe league all moves to designated areas, You could do what your told and go to the dorms, but you could also do something else.\n\n";
    std::cout << "1.)Naw, Ima do what i was told to do and fight the kids\n2.)Im going to go with twice's team\n3.)Im going to go alert the hero's of the attack\n4.)I saw endeavors agency close here, ima go fight endeavor instead.\nEnter your input: ";
    std::cin >> input;
    if (input == 4) {
        std::cout << "(You went to endeavors agency)\nEndeavor:What do you want punk?\n" << name << ":lets fight!\n Endeavor:lets get this over with.\n";
        for (int x = 100, y = 100; x != 0;) {
            int move = 0;
            std::cout << "Endeavor health: " << y << "    " << name << " health: " << x << "\n";
            std::cout << "1.)Kick\n2.)punch\n3.)Dodge\nEnter your move against endeavor:";
            std::cin >> move;
            if (move > 3 || move < 0) {
                std::cout << "You just sat there!\n";
            }
            else {
                if (move == 1) {
                    std::cout << "You used a kick! it did 1 points of damage!\n";
                    y--;
                    std::cout << "Endeavor health: " << y << "\n" << name << " health: " << x << "\n";
                }
                else if (move == 2) {
                    std::cout << "You used a punch! it did 1 points of damage!\n";
                    y--;
                    std::cout << "Endeavor health: " << y << "\n" << name << " health: " << x << "\n";
                }
                else if (move == 3) {
                    std::cout << "You prepared to dodge an attack!\n";
                }
                if (move == 3) {
                    std::cout << "You tried to dodge but you couldn't move fast enough! Endeavor used jet burn! it did " << x << " points!\n";
                    dead = "yes";
                    x = x - x;
                }
                else {
                    std::cout << "Endeavor used jet burn! it did " << x << " points!\n";
                    dead = "yes";
                    x = x - x;
                }
            }
        }
        if (dead == "yes") {
            std::cout << "YOU DIED!\n";
            abort();

        }
    }
    else if (input == 1) {
        std::cout << "(You went to the dorms and defeated most of them with ease, but monoma and tetsu tetsu proved difficult\ntetsu tetsu:COME AT ME VILLIAN!!\n";
        shigaraki++;
        myFunction(76, 100, "Tetsu Tetsu", name, 14, 19);
        std::cout << "Monoma:He was easy, now comes the hard part!\n";
        myFunction(86, 103, "Monoma", name, 16, 21);
        std::cout << "Monoma:Damn,Your too strong\nTetsu Tetsu:Damn it! just make it quick!";
        std::cout << "\n\n(You could kill them along with the rest of the defeated 1B students, but somethings telling you to spare them\n";
        std::cout << "1.)Yes, i'll spare them\n2.)No, I should just kill them\n3.)I dont feel like killing them but i dont wanna get in trouble with shigaraki, into the dumpster with them\nEnter you choice:";
        std::cin >> input;
        bool valid = true;
        if (input < 0 || input > 3) {
            bool valid = false;
            while (valid == false) {
                std::cout << "Dont just sit there, you gotta pick 1!";
                std::cin >> input;
                if (input == 1) {
                    std::cout << name << ":You guys get to survive today, be thankful\n";
                    AM++;
                    valid = true;
                }
                else if (input == 2) {
                    std::cout << name << ":you guys picked the wrong side\n";
                    shigaraki++;
                    valid = true;
                }
                else if (input == 3) {
                    std::cout << name << ":Ima just leave you in the dumpster and call it a day\nMonoma:And so we survive a villain once again!\n";
                    decide++;
                    valid = true;
                }
            }
        }
        else if (input == 1) {
            std::cout << name << ":You guys get to survive today, be thankful\n";
            AM++;
        }
        else if (input == 2) {
            std::cout << name << ":you guys picked the wrong side\n";
            shigaraki++;
        }
        else if (input == 3) {
            std::cout << name << ":Ima just leave you in the dumpster and call it a day\nMonoma:And so we survive a villain once again!\n";
            decide++;
        }
    }
    else if (input == 2) {
        std::cout << "(You decided to go with twice, But you ran into kirishima on the way!\nkirishima:Got a few questions for you!\n";
        decide++;
        myFunction(79, 100, "kirishima", name, 6, 23);
        std::cout << "Kirishima:Im out! gotta warn the others!\n(He was too fast for you)\nyou found Twice, Deku and Dynamight in the UA stadium)\nTwice:YOU KIDS ARE TOUGH!(you kids are weak as hell)\nDeku:kacchan, keep blasting those clones fatser than he can make them!\nDynamight:Shut up!\nTwice: " << name << "!? Your suppose to be at the 1B dorms!(who are ya???) Well, it dont matter! help me out with the explosive dude!\n";
        std::cout << "Dynamight:Who the hell are you?\n" << name << ":My names " << name << "!\nDynamight:Shut dumbass, all i know is that you gonna die you extra!";
        myFunction(98, 103, "Dynamight", name, 17, 25);
        std::cout << "Dynamight:Damn! how'd I get beat by an extra! Deku how you holding up!?\nDeku:the clones... were too much! gotta run!\nTwice:Dang, he got away! Goodwork " << name << "!\n" << name << ":You look hurt, you ok?\nTwice:I'm fine, OFA is not joke!  guest of wind could kill me right about now!\n";
        std::cout << "\n\nEveryone but you is on the verge of defeat or is already defeated,you could help twice heal his wounds, or you could kill twice, you could also just leave everyone him alone and let him finish off Dynamight";
        std::cout << "\n1.)I'll help twice\n2.)I'll kill twice\n3.)I'll just sit and watch\nEnter you choice:";
        std::cin >> input;
        bool valid = true;
        if (input < 0 || input > 3) {
            bool valid = false;
            while (valid == false) {
                std::cout << "Dont just sit there, you gotta pick 1!";
                std::cin >> input;
                if (input == 1) {
                    std::cout << name << ":Ok twice, lets get you patched up!\nTwice:Thanks(screw you) Ima finish off this explosion brat\n";
                    shigaraki++;
                    valid = true;
                }
                else if (input == 2) {
                    std::cout << name << ":Don't trust the first person you meet, twice\nTwice:Wait what..?\nyou killed twice and let Dynamight live, he'll probably go where deku is going\n";
                    tdead = true;
                    AM++;
                    valid = true;
                }
                else if (input == 3) {
                    std::cout << name << ":Ima just sit here, tell me when your done\nTwice: Damn not even a little concern? oh well, let me take care of explosion boy real quick\n";
                    decide++;
                    valid = true;
                }
            }
        }
        else if (input == 1) {
            std::cout << name << ":Ok twice, lets get you patched up!\nTwice:Thanks(screw you) Ima finish off this explosion brat\n";
            shigaraki++;
        }
        else if (input == 2) {
            std::cout << name << ":Don't trust the first person you meet, twice\nTwice:Wait what..?\nyou killed twice and let Dynamight live, he'll probably go where deku is going\n";
            tdead = true;
            AM++;
        }
        else if (input == 3) {
            std::cout << name << ":Ima just sit here, tell me when your done\nTwice: Damn not even a little concern? oh well, let me take care of explosion boy real quick\n";
            decide++;
        }

    }
    else if (input == 3) {
        std::cout << "(You decided that the hero association need to be warned about the attack on UA, but as you were on the phone with them you heard Mr.compress yell out to you!\nMr.Compress:I told twice you were a bad idea, now look. Any moment now the hero's and maybe endeavor might show up and cut our show short!\n" << name << ":No regrets\nMr.compress:Well your about to have some\n";
        AM++;
        myFunction(79, 100, "Mr.Compress", name, 15, 18);
        std::cout << "Mr.Compress: Damn! Gotta think fast!\n" << name << ":Your done\nMr.Compress:oh yeah! i still got the mid-tier Nomu from the UA camp attack! good luck defeating this big guy\nchainsaw-Nomu:uhhhhh\n";
        myFunction(90, 103, "chainsaw-Nomu", name, 18, 20);
        std::cout << "Mr.Compress:...\nMr.Compress is speechless and the option of killing him is right there, but do you really want to finish him?\n";
        std::cout << "1.)Kill him\n2.)it's like hes a threat, but might as well restrain him so the others don't find out\n3.)leave him alive, but put a bomb inside his mouth, that'll take him out and the hero's that should be arriving\n";
        std::cin >> input;
        if (input < 0 || input > 3) {
            bool valid = false;
            while (valid == false) {
                std::cout << "Dont just sit there, you gotta pick 1!";
                std::cin >> input;
                if (input == 1) {
                    std::cout << name << ":Sorry but not sorry, Compress!\n";
                    cdead = true;
                    AM++;
                    valid = true;
                }
                else if (input == 2) {
                    std::cout << name << ":I aint gonna kill you, i like you too much, but can't risk the others finding out, so ima just leave you in the dumpster\nMr.Compress:I always knew i was too charming to die, but screw you!\nyou left Mr.Compress in the dumpster, it's better than being dead i guess\n";
                    comcap = true;
                    shigaraki++;
                    valid = true;
                }
                else if (input == 3) {
                    std::cout << name << ":You know, using you as a trap to take down the hero's on their way. You like the taste of bombs?\nMr.Compress:You ant the kill the hero's YOU called???? Psycho.\nYou stuffed the bomb in his mouth and left him outside UA, the hero's are in for a treat\n";
                    cdead = true;
                    decide++;
                    valid = true;
                }
            }
        }
        else if (input == 1) {
            std::cout << name << ":Sorry but not sorry, Compress!\n";
            cdead = true;
            AM++;
        }
        else if (input == 2) {
            std::cout << name << ":I aint gonna kill you, i like you too much, but can't risk the others finding out, so ima just leave you in the dumpster\nMr.Compress:I always knew i was too charming to die, but screw you!\nyou left Mr.Compress in the dumpster, it's better than being dead i guess\n";
            comcap = true;
            shigaraki++;
        }
        else if (input == 3) {
            std::cout << name << ":You know, using you as a trap to take down the hero's on their way. You like the taste of bombs?\nMr.Compress:You ant the kill the hero's YOU called???? Psycho.\nYou stuffed the bomb in his mouth and left him outside UA, the hero's are in for a treat\n";
            cdead = true;
            decide++;
        }
    }
    else {
        std::cout << "Unsure of what to do, you killed yourself\nYOU DIED";
        abort();
    }
    std::cout << "\nShigaraki:Hey! everybody group up near the principles office!\n(You all decide to gather where he said)\n\n";
    if (cdead == true || comcap == true) {
        std::cout << "Where is Mr.compress?\nToga: i dont know, he said he had a bad feeling and went back to the entrance to check something\nDabi:That was stupid, he probably got jumped by some 3rd years\nSpinner:It's ok, we'll get him back\nShigaraki:Yeah, we can't leave someone behind, but for now we must complete the mission\n";
    }
    else if (tdead == true) {
        std::cout << "Where is Twice?\nMr.Compress:Heard some screaming coming from twice's area, also saw explosion boy feeling the area, they likely got twice arrested\nShigaraki:It's ok, we'll get him back\nToga:Yeah, we can't leave him behind\n Shigaraki:but for now we must complete the mission,anyone get deku yet?\n";
    }
    else {
        std::cout << "Shigaraki: Glad everyones here in one peace!\n";
    }
    std::cout << "Shigaraki:So, anyone capture deku yet?\nDabi:I can answer that, seeing as i saw the kid running away on our way here i can tell that none of us were able to get him\nShigaraki:He couldn't have gone far, " << name << ",Dabi, you guys go and retrieve him.\nDabi:He wounded so we should be able to handle it, might even run into shoto.\n\n(you both make your way to where he fled, you know, dabi and you are all by yourself.\n\n1.)Take him out\n2.)Naw,lets go get deku\n3.)Let him go take deku, I can 'stand guard' aka do nothing cause i don't feel like getting involved in this\nEnter you answer:";
    std::cin >> input;
    if (input < 0 || input > 3) {
        if (quiet == 1) {
            std::cout << "(You just stood there, not saying or doing anything)\nDabi:hey kid, you good??\n\n(Suddenley your transported to a room, and you see a dude with a blindfold and white hair\nGojo:So, you figured out the way to escape this world, your options on what to do are presented in numbers right? type 10/31 to enter your final challange\n";
            quiet++;
            std::cout << "Dabi:Hello??\n" << name << ":Oh... Sorry\nDabi:Since you obisously have brain damage you stand guard, ill get deku\n";
            std::cout << "(You wait just doing nothing, but suddenly a figure approaches)\nTamaki:St-st-stop there!\n" << name << ":You look frail, just hope y'know what your getting yourself into\n";
            myFunction(98, 106, "Tamaki", name, 17, 26);
            std::cout << "\n(You got a good hit in, he died muttering something about, 'brighter than the sun'\nDabi:I got the kid, lets head back to shigaraki";
        }
        else {
            std::cout << "\n(After standing there and thinking for a good minute, you decided that you did feel like doing anything)\n" << name << ":You go ahead! i need to stay guard\nDabi:Aka your lazy, fuck you. Just don't get caught\n\n(You wait just doing nothing, but suddenly a figure approaches)\nTamaki:St-st-stop there!\n" << name << ":You look frail, just hope y'know what your getting yourself into\n";
            decide++;
            myFunction(98, 106, "Tamaki", name, 17, 26);
            std::cout << "\n(You got a good hit in, he died muttering something about, 'brighter than the sun'\nDabi:I got the kid, lets head back to shigaraki";
            dcaptu = true;
        }
    }
    else if (input == 1) {
        std::cout << name << ":Hey dabi?\nDabi:?\n" << name << ":Roll over and die will ya?\nDabi:you'd better be joking, after all if your a stinky traitor i'll have to fry you\n" << name << ":Im for real :)\nDabi...\nDabi:Then fry you piece of crap\n";
        AM++;
        myFunction(97, 106, "Dabi", name, 12, 28);
        std::cout << "(You got a fatal hit on him during the fight, he lays there dying)\nDabi:Looks like...I waited too long...To tll endeavor about my survival...\n(he passes away, all your thinking is 'what was that about endeavor?'\n";
    }
    else if (input == 2) {
        std::cout << name << ":We almost at the location?\nDabi:Yeah were almost-\nTamaki:St-st-stop there!\nDabi:looks what i'v found" << name << "! G-A-R-B-A-G-E\nDabi:i'll take care of the garbage you go get deku!\n";
        shigaraki++;
        std::cout << "\n(You went to go look for deku and found him bleeding over a knocked out bakugo)\nDeku:Damn, that twice guy was rough! dont worry kacchan i'll get us outta here!\n" << name << ":Sorry to burst you bubble but you aint making it out of here\nDeku:Im sorry, but you'll have to get out of my way!\n";
        myFunction(98, 106, "Deku", name, 14, 29);
        std::cout << "Deku: Damn...i lost\n(He passed out)\n\nDabi:The trash's burnt, you got the kid?\n" << name << ":Yeah, he's tougher than he looks\nDabi:Well, let get him out of here and to shigaraki\n";
        dcaptu = true;
    }
    else if (input == 3) {
        std::cout << name << ":You go ahead! i need to stay guard\nDabi:Aka your lazy, fuck you. Just don't get caught\n\n(You wait just doing nothing, but suddenly a figure approaches)\nTamaki:St-st-stop there!\n" << name << ":You look frail, just hope y'know what your getting yourself into\n";
        decide++;
        myFunction(98, 106, "Tamaki", name, 17, 26);
        std::cout << "\n(You got a good hit in, he died muttering something about, 'brighter than the sun'\nDabi:I got the kid, lets head back to shigaraki";
        dcaptu = true;
    }

    if (dcaptu != true) {
        std::cout << "Shigaraki: " << name << "is back!\nToga:But wheres dabi and deku-kun?\n" << name << ": That kid hit us with a '100% detriot smash' over and over again, dabi didn't make it...\nShigaraki:Damn! Im gonna kill that mf!\n\n";
    }
    else {
        std::cout << "Shigaraki: " << name << "and dabi are back!\nDeku:uhhh\nToga:Its deku-kun!\nDabi:He was easier than i thought\n" << name << ": Time to head back now?\nShigaraki:Sur-\n";
    }
    std::cout << "Endeavor:I am here... \n(Dramatic landing sound while hawks and best jeanist appear behind him)\nEndeavor;TO kick ass!\nShigaraki:but...how?\n";
    if (cdead == true) {
        std::cout << "Endeavor:We got an anonymous call\n";
    }
    else {
        std::cout << "Best jeanist: Great explosion god dynamight warned us!\n";
    }

    std::cout << "Shigaraki:Damn! everyone hurry and get ready to battle!\n";
    if (AM > shigaraki && AM > decide) {
        winner = "AM";
    }
    else if (shigaraki > AM && shigaraki > decide) {
        winner = "shigaraki";
    }
    else {
        winner = "decide";
    }
    if (winner == "decide") {
        std::cout << "\nAs everyone prepares to fight, you stand in the middle, you want to help the hero's but somethings telling you to help the hero's instead, what will it be, " << name << "?\n";
        std::cout << "1.) Help the hero's\n2.) Help the villains\n";
        std::cin >> input;
        if (input < 0 || input > 2) {
            bool valid = false;
            while (valid == false) {
                std::cout << "This is too important to just stand there, don't you think?";
                std::cin >> input;
                if (input == 1) {
                    winner = "AM";
                }
                else if (input == 2) {
                    winner = "shigaraki";
                }
            }
        }
        else if (input == 1) {
            winner = "AM";
        }
        else if (input == 2) {
            winner = "shigaraki";
        }
    }
    if (quiet == 2) {
        std::string code;
        std::cout << "\nYou stand there, you look to both directions and say nothing, you suddenly enter a room and the guy with the hair is there again\nGojo:Looks like you made it, before we can begin, tell me the code";
        std::cin >> code;
        if (code != "10/31") {
            std::cout << "Gojo: You screwed up, sorry to inform you but i have to kill you now\n";
            for (int x = 100, y = 100; x != 0;) {
                int move = 0;
                std::cout << "Gojo health: " << y << "    " << name << " health: " << x << "\n";
                std::cout << "1.)Kick\n2.)punch\n3.)Dodge\nEnter your move against endeavor:";
                std::cin >> move;
                if (move > 3 || move < 0) {
                    std::cout << "You just sat there!\n";
                }
                else {
                    if (move == 1) {
                        std::cout << "You used a kick! it did 1 points of damage!\n";
                        y--;
                        std::cout << "Gojo health: " << y << "\n" << name << " health: " << x << "\n";
                    }
                    else if (move == 2) {
                        std::cout << "You used a punch! it did 1 points of damage!\n";
                        y--;
                        std::cout << "Gojo health: " << y << "\n" << name << " health: " << x << "\n";
                    }
                    else if (move == 3) {
                        std::cout << "You prepared to dodge an attack!\n";
                    }
                    if (move == 3) {
                        std::cout << "You tried to dodge but you couldn't move fast enough! Gojo used hallow purple! it did " << x << " points!\n";
                        dead = "yes";
                        x = x - x;
                    }
                    else {
                        std::cout << "Gojo used hallow purple! it did " << x << " points!\n";
                        dead = "yes";
                        x = x - x;
                    }
                }
            }
            if (dead == "yes") {
                std::cout << "YOU DIED!\n";
                abort();

            }
        }
        else {
            std::cout << "Gojo: Good! though i was gonna have to kill you!, ok. Now to explain, you've been transported to the anime universe because the ani gods rolled a dice and landed on you, by being quiet you can escape, and you did just that, but now you have to fight a slew a people from this universe to finally go home, in order to make things fair you now have a health of 320, good luck!\n";
            myFunction(80, 340, "Mirio", name, 19, 12);
            std::cout << "Gojo: Next!\n";
            myFunction(100, 340, "Overhaul", name, 10, 32);
            std::cout << "Gojo: You on a roll!\n";
            myFunction(138, 340, "Number 6", name, 21, 28);
            std::cout << "Gojo: Next!\n";
            myFunction(160, 340, "Hood", name, 30, 30);
            std::cout << "Gojo: That was tough!\n";
            myFunction(200, 340, "Machia", name, 42, 30);
            std::cout << "Gojo: Warmer!\n";
            myFunction(275, 340, "All for one", name, 11, 44);
            std::cout << "Gojo: Last one!\n";
            myFunction(305, 340, "All might", name, 35, 39);
            std::cout << "\n\nAs all might goes down, you sit there on the verge of passing out\nGojo:Good job, i thought you would die!\nGojo: Well buddy, ready to go home?" << name << ":...\nGojo:Good, you passed the final test, if you responded I'd have killed you\n\nYou wake up in your bed, your relived, but then you realize that it's amonday, you have 10 missing assignments and are now 10 minutes late, to add to that one of your friends is mad at you for who knows what now, AND you need to suck up to your entitled siblings. You miss the my hero academia world and want to go back, but you can't :(";
            system("PAUSE");

        }
    }
    else if (winner == "AM") {
        std::cout << name << ": Im sorry shigaraki, but im no villain.\nShigaraki:...\n";
        if (cdead == true) {
            std::cout << name << ": I killed compress and called the hero's\n";
        }
        else if (comcap == true) {
            std::cout << name << ": I defeated compress\n";
        }
        if (tdead == true) {
            std::cout << name << ": I killed twice\n";
        }
        if (dcaptu != true) {
            std::cout << name << ":Dabi's now taking a nice nap\n";
        }
        std::cout << "Shigaraki: You little shit! You guys! Take out the other 2! " << name << "is all mine.\nHawks:Good luck with that!\nShigaraki:Lets end this, " << name << "!\n";
        myFunction(125, 140, "Shigaraki", name, 20, 32);
        std::cout << "Shigaraki: I should've... let you die!\n\n(Shigaraki died and the remain league was defeated)\nHawks:Hey, good work nameless dude\nEndeavor: Your still under arrest, but with your actions today you might just be let off free\n";
        if (dcaptu == true) {
            std::cout << "Deku: Wish you grand plan of defeating them didn't include me getting bloodied up!\n";
        }
        std::cout << "\n\nYou were let of the hook, after that you enrolled at UA as a 2nd year, and began you new life as a hero!";
        system("PAUSE");
    }
    else if (winner == "shigaraki") {
        std::cout << name << ": y'know, i didn't like any of you at first, but i'v grown attached! i won't let it end here!\nEndeavor: You both take out the league, i need to deal with this kid!\n";
        myFunction(122, 140, "Endeavor", name, 23, 29);
        std::cout << "\n(The league defeated the hero's, thank god)\nShigaraki: You took out Endeavor!\nSpinner: Looks like we get even stronger with you!\n";
        if (comcap == true) {
            std::cout << name << ": Before we go, lets go get compress\nToga:What you know where he is?\n" << name << ": Well wasn't sure, I kinda attack and put him in the trash..\nShigaraki:You better beg for his forgivingness, i dont care though as long as hes alive\n";
        }
        if (cdead == true || tdead == true || dcaptu != true) {
            std::cout << name << ": Hope the League never find out about what i did(the whole secrete killing thing)\n";
        }
        if (dcaptu != true) {
            std::cout << "Toga: What about deku-kun?\nShigaraki: Doesn't matter, I'll go after him once my surgery is done\n";
        }
        else {
            std::cout << "Deku: You guys will... never get away with this!\nDabi: Once shigaraki is done with the surgery, we will have the power of One For All, the world will be at our palms\n";

        }
        std::cout << "\n\nYour new life as a villain began, and you prepared yourself for all that waits you as you walk towards the destruction of society!\n";
        system("PAUSE");
    }
}
