// you should be able to finish, finish adding ties in the win function and add computer to the code

#include <iostream>
#include <vector>
#include <string>
#include "Header.h"
int main()
{
    std::string onename;
    std::string twoname;
    int onewins = 0;
    int twowins = 0;
    int oneloses = 0;
    int twoloses = 0;

    std::cout << "What is player 1's name?";
    std::cin >> onename;
    std::cout << "What is player 2's name?";
    std::cin >> twoname;
    bool ov = false;
    std::string again{};
    while (ov == false) {
        bool what = false;
        std::string y = game(board, onename, twoname);
        if (y == onename) {
            std::cout << onename << " Wins!\n";
            onewins++;
            twoloses++;
        }
        else if (y == twoname) {
            std::cout << twoname << " Wins!\n";
            twowins++;
            oneloses++;
        }
        else if (y == "Tie!") {
            std::cout << "Its a tie!\n";
        }
        std::cout << onename << " Wins: " << onewins << " Loses: " << oneloses << "\n" << twoname << " Wins: " << twowins << " Loses: " << twoloses << "\n\nWould you like to play again?";
        std::cin >> again;
        if (again == "yes") {
            std::cout << "Time for the next round!\n";
            reset();
        }
        else if (again == "no") {
            std::cout << "Goodbye\n";
            ov = true;
        }
        else {
            what = true;
        }
        while (what == true) {
            std::cout << "Invalid choice, either yes or no";
            std::cin >> again;
            if (again == "yes") {
                std::cout << "Time for the next round!\n";
                reset();
                what = false;
            }
            else if (again == "no") {
                std::cout << "Goodbye\n";
                ov = true;
                what = false;
            }
            else {
                what = true;
            }
        }
    }
}