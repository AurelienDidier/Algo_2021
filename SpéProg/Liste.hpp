/*
 * Liste.hpp
 *
 *  Created on: 7 févr. 2022
 *      Author: GAME1.1
 */

#ifndef LISTE_HPP_
#define LISTE_HPP_

#include "Maillon.hpp"

class Liste{

private:
	Maillon * premier;
public:
	Liste();
	~Liste();
	Liste(int tab[], int size);
	int getLongueur();
	void ajoutApres(int valeur);
	void ajoutDebut(int valeur);
};



#endif /* LISTE_HPP_ */
