#include <iostream>
#include <vector>
#include <random>
#include <string>
#include <algorithm>

std::string playerone{};
std::string playertwo{};
char playeronesign{};
char playertwosign{};
std::vector<std::string> board = { "_"," _"," _\n","_"," _"," _\n","_"," _"," _" };
std::vector<int> boardindx = {0,1,2,3,4,5,6,7,8};
std::string tie{};

inline
bool win(std::string player) {
    int win = 0;
    std::vector<std::string> toard = board;
    for (auto& str : toard) {
        str.erase(std::remove(str.begin(), str.end(), ' '), str.end());
    }
    for (auto& str : toard) {
        str.erase(std::remove(str.begin(), str.end(), '\n'), str.end());
    }
    int yu = 0;
    for (int x = 0; x < toard.size(); x++) {
        if (yu == 3 && win <= 2) {
            win = 0;
            yu = 0;
        }
        if (player == toard[x]) {
            win++;
            if (win == 3) {
                return true;
            }
        }
        else {
            win = 0;
        }
        yu++;
    }
    win = 0;
    int tied = 0;

    int tin = 0;
    for (int d = 0; d < 3; d++) {
        if (toard[tin] == player) {
            win++;
            if (win == 3) {
                return true;
            }
        }
        else {
            win = 0;
        }
        tin = tin + 3;
    }
    tin = 1;
    win = 0;
    for (int d = 0; d < 3; d++) {
        if (toard[tin] == player) {
            win++;
            if (win == 3) {
                return true;
            }
        }
        else {
            win = 0;
        }
        tin = tin + 3;
    }
    tin = 2;
    win = 0;
    for (int d = 0; d < 3; d++) {
        if (toard[tin] == player) {
            win++;
            if (win == 3) {
                return true;
            }
        }
        else {
            win = 0;
        }
        tin = tin + 3;
    }
    win = 0;

    
    if (toard[0] == player) {
        win++;
    }
    else {
        win = 0;
    }

    if (toard[4] == player) {
        win++;
    }
    else {
        win = 0;
    }

    if (toard[8] == player) {
        win++;
    }
    else {
        win = 0;
    }
    if (win == 3) {
        return true;
    }
    else {
        win = 0;
    }
    win = 0;

    if (toard[2] == player) {
        win++;
    }
    else {
        win = 0;
    }

    if (toard[4] == player) {
        win++;
    }
    else {
        win = 0;
    }

    if (toard[6] == player) {
        win++;
    }
    else {
        win = 0;
    }

    if (win == 3) {
        return true;
    }
    else {
        win = 0;
    }
    win = 0;

    for (int x = 0; x < toard.size(); x++) {
        if ("x" == toard[x] || "y" == toard[x]) {
            tied++;
        }
    }
    if (tied == 9) {
        tie = "Tie!";
        return true;
    }
    else {
        win = 0;
        return false;
    }
}

inline
void game_status() {
    for (int x = 0; x < board.size(); x++) {
        std::cout << board[x];
    }

    std::cout << "\n\n" << playerone << " sign: " << playeronesign << "\n" << playertwo << " sign: " << playertwosign << "\n\n";
}

inline
bool place(std::string goingfirst) {
    int put{};
    bool valid = true;
    if (goingfirst == playerone) {
        std::cout << "Where do you want to place your " << playeronesign << " " << playerone << "?";
        std::cin >> put;
        if (put < 1 || put > 9) {
            valid = false;
        }
        else {
            put--;
            if (std::count(boardindx.begin(), boardindx.end(), put)) {
                std::cout << "";
            }
            else {
                std::cout << "That square is already taken\n";
                valid = false;
            }
        }
        if (valid != false) {
            if (board[put] == "_") {
                char u = playeronesign;
                std::string s(1, u);
                board[put] = s;
                boardindx.erase(std::remove(boardindx.begin(), boardindx.end(), put), boardindx.end());
                if (win(s) == true) {
                    return true;
                }
                else {
                    return false;
                }
                valid = true;
            }
            if (board[put] == " _") {
                char u = playeronesign;
                std::string s(1, u);
                board[put] = " " + s;
                boardindx.erase(std::remove(boardindx.begin(), boardindx.end(), put), boardindx.end());
                if (win(s) == true) {
                    return true;
                }
                else {
                    return false;
                }
                valid = true;
            }
            else if (board[put] == " _\n") {
                char u = playeronesign;
                std::string s(1, u);
                board[put] = " " + s + "\n";
                boardindx.erase(std::remove(boardindx.begin(), boardindx.end(), put), boardindx.end());
                if (win(s) == true) {
                    return true;
                }
                else {
                    return false;
                }
                valid = true;
            }
        }
        while (valid == false) {
            std::cout << "Invalid choice, try again.";
            std::cin >> put;
            if (put < 1 || put > 9) {
                valid = false;
            }
            else {
                put--;
                if (std::count(boardindx.begin(), boardindx.end(), put)) {
                    std::cout << "";
                }
                else {
                    std::cout << "That square is already taken\n";
                    valid = false;
                }
            }
            if (valid == false) {
                if (board[put] == "_") {
                    char u = playeronesign;
                    std::string s(1, u);
                    board[put] = s;
                    boardindx.erase(std::remove(boardindx.begin(), boardindx.end(), put), boardindx.end());
                    if (win(s) == true) {
                        return true;
                    }
                    else {
                        return false;
                    }
                    valid = true;
                }
                else if (board[put] == " _") {
                    char u = playeronesign;
                    std::string s(1, u);
                    board[put] = " " + s;
                    boardindx.erase(std::remove(boardindx.begin(), boardindx.end(), put), boardindx.end());
                    if (win(s) == true) {
                        return true;
                    }
                    else {
                        return false;
                    }
                    valid = true;
                }
                else if (board[put] == " _\n") {
                    char u = playeronesign;
                    std::string s(1, u);
                    board[put] = " " + s + "\n";
                    boardindx.erase(std::remove(boardindx.begin(), boardindx.end(), put), boardindx.end());
                    if (win(s) == true) {
                        return true;
                    }
                    else {
                        return false;
                    }
                    valid = true;
                }
            }
        }
    }
    else if (goingfirst == playertwo) {
        std::cout << "Where do you want to place your " << playertwosign << " " << playertwo << "?";
        std::cin >> put;
        if (put < 1 || put > 9) {
            valid = false;
        }
        else {
            put--;
            if (std::count(boardindx.begin(), boardindx.end(), put)) {
                std::cout << "";
            }
            else {
                std::cout << "That square is already taken\n";
                valid = false;
            }
        }
        if (valid != false) {
            if (board[put] == "_") {
                char u = playertwosign;
                std::string s(1, u);
                board[put] = s;
                boardindx.erase(std::remove(boardindx.begin(), boardindx.end(), put), boardindx.end());
                if (win(s) == true) {
                    return true;
                }
                else {
                    return false;
                }
                valid = true;
            }
            else if (board[put] == " _") {
                char u = playertwosign;
                std::string s(1, u);
                board[put] = " " + s;
                boardindx.erase(std::remove(boardindx.begin(), boardindx.end(), put), boardindx.end());
                if (win(s) == true) {
                    return true;
                }
                else {
                    return false;
                }
                valid = true;
            }
            else if (board[put] == " _\n") {
                char u = playertwosign;
                std::string s(1, u);
                board[put] = " " + s + "\n";
                boardindx.erase(std::remove(boardindx.begin(), boardindx.end(), put), boardindx.end());
                if (win(s) == true) {
                    return true;
                }
                else {
                    return false;
                }
                valid = true;
            }
        }
        while (valid == false) {
            std::cout << "Invalid choice, try again.";
            std::cin >> put;
            if (put < 1 || put > 9) {
                valid = false;
            }
            else {
                put--;
                if (std::count(boardindx.begin(), boardindx.end(), put)) {
                    std::cout << "";
                }
                else {
                    std::cout << "That square is already taken\n";
                    valid = false;
                }
            }
            if (valid == false) {
                if (board[put] == "_") {
                    char u = playertwosign;
                    std::string s(1, u);
                    board[put] = s;
                    boardindx.erase(std::remove(boardindx.begin(), boardindx.end(), put), boardindx.end());
                    if (win(s) == true) {
                        return true;
                    }
                    else {
                        return false;
                    }
                    valid = true;
                }
                else if (board[put] == " _") {
                    char u = playertwosign;
                    std::string s(1, u);
                    board[put] = " " + s;
                    boardindx.erase(std::remove(boardindx.begin(), boardindx.end(), put), boardindx.end());
                    if (win(s) == true) {
                        return true;
                    }
                    else {
                        return false;
                    }
                    valid = true;
                }
                else if (board[put] == " _\n") {
                    char u = playertwosign;
                    std::string s(1, u);
                    board[put] = " " + s + "\n";
                    boardindx.erase(std::remove(boardindx.begin(), boardindx.end(), put), boardindx.end());
                    if (win(s) == true) {
                        return true;
                    }
                    else {
                        return false;
                    }
                    valid = true;
                }
            }
        }
    }
    return false;

}

inline
std::string game(std::vector<std::string>board,std::string onename,std::string twoname) {
    std::random_device dev;
    std::mt19937 rng(dev());
    char playersign{};
    char ensign{};
    int numplaymov = 0;
    playerone = onename;
    playertwo = twoname;

    std::cout << "What do you want to be? X or Y?";
    std::cin >> playersign;
    if ((playersign != 'x') && (playersign != 'y')) {
        std::uniform_int_distribution<std::mt19937::result_type> dist6(1, 2);
        int ran = dist6(rng);
        if (ran == 1) {
            std::cout << "You put an invalid answer, you shall be x\n";
            playersign = 'x';
        }
        else if (ran == 2) {
            std::cout << "You put an invalid answer, you shall be y\n";
            playersign = 'y';
        }
    }
    if (playersign == 'x') {
        ensign = 'y';
    }
    else if (playersign == 'y') {
        ensign = 'x';
    }
    std::cout << "\n";

    playeronesign = playersign;
    playertwosign = ensign;
    game_status();

    bool over = false;
    bool yeg = false;
    int numfirst{};
    std::string first{};
    std::cout << "\nChoose 1 or 2:";
    std::cin >> numfirst;
    if (numfirst < 1 || numfirst > 2) {
        yeg = true;
    }
    while (yeg == true) {
        std::cout << "Invalid choice, pick 1 or 2:";
        std::cin >> numfirst;
        if (numfirst < 1 || numfirst > 2) {
            yeg = true;
        }
        else {
            yeg = false;
        }
    }
    std::uniform_int_distribution<std::mt19937::result_type> dist6(1, 2);
    int ling = dist6(rng);
    if (numfirst == ling) {
        std::cout << onename << " is going first\n";
        first = onename;
    }
    else {
        std::cout << twoname << " is going first\n";
        first = twoname;
    }

    bool tover = false;
    std::vector<std::string> cho = {playerone,playertwo};
    int in = 0;
    std::string winner{};
    place(first);
    game_status();
    if (first == cho[0]) {
        in = 1;
    }
    else {
        in = 0;
    }
    while (tover != true) {
        bool r = place(cho[in]);
        if (r == true && boardindx.empty() == true) {
            winner = "tie";
            tover = true;
        }
        if (r == true && tie == "Tie!") {
            game_status();
            winner = "Tie!";
            tover = true;
        }
        else if (r == true && in == 0) {
            game_status();
            winner = playerone;
            tover = true;
        }
        else if (r == true && in == 1) {
            game_status();
            winner = playertwo;
            tover = true;
        }
        else {
            game_status();
            if (in == 0) {
                in++;
            }
            else {
                in = 0;
            }
        }
    }
    return winner;
    
}

void reset() {
    board = { "_"," _"," _\n","_"," _"," _\n","_"," _"," _" };
    boardindx = { 0,1,2,3,4,5,6,7,8 };
    tie = "";
}
