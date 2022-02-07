/*
 * Maillon.cpp
 *
 *  Created on: 7 févr. 2022
 *      Author: GAME1.1
 */

#include "Maillon.hpp"

inline Maillon::Maillon(){
	valeur = 0 ;
	suivant = nullptr;
}

inline Maillon * Maillon::getSuivant(){
	return suivant;
}
inline void Maillon::setSuivant(Maillon * suiv){
	suivant = suiv;
}
inline int Maillon::getValue(){
	return valeur;
}
inline void Maillon::setValeur(int val){
	valeur = val;
}



