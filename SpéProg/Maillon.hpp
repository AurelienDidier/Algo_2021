/*
 * Maillon.hpp
 *
 *  Created on: 7 févr. 2022
 *      Author: GAME1.1
 */

#ifndef MAILLON_HPP_
#define MAILLON_HPP_

class Maillon {
private:
	int valeur;
	Maillon * suivant;
public:
	Maillon();
	Maillon * getSuivant();
	void setSuivant(Maillon * suivant);
	int getValue();
	void setValeur(int valeur);
};



#endif /* MAILLON_HPP_ */
