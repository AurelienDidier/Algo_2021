/*
 * Liste.cpp
 *
 *  Created on: 7 févr. 2022
 *      Author: GAME1.1
 */
#include "Liste.hpp"
inline Liste::Liste(){
	this->premier = nullptr;
}

inline Liste::~Liste(){
	Maillon * courant = this->premier;
	Maillon * precedent = this->premier;
	while ( courant->getSuivant()!= nullptr ){
		precedent = courant;
		courant = courant->getSuivant();
		delete precedent;
	}
	delete courant;
}

inline Liste::Liste(int tab[], int size){
	this->premier = new Maillon;
	Maillon * precedent = premier;
	for (int i = 0; i <size; i++){
		Maillon * courant = new Maillon;
		courant->setValeur(tab[i]);
		precedent->setSuivant(courant);
		precedent = courant;
	}
}

inline int Liste::getLongueur(){
	Maillon * courant = this->premier;
	int taille = 0;
	while ( courant!= nullptr ){
		courant = courant->getSuivant();
		taille++;
	}
	return taille;
}

void inline Liste::ajoutApres(int valeur){
	Maillon * courant = this->premier;
	while ( courant->getSuivant()!= nullptr ){
		courant = courant->getSuivant();
	}
	Maillon * nouveau = new Maillon;
	nouveau->setValeur(valeur);
	courant->setSuivant(nouveau);

}

void inline Liste::ajoutDebut(int valeur){
	Maillon * nouveau = new Maillon;
	nouveau->setValeur(valeur);
	nouveau->setSuivant(this->premier);
	this->premier = nouveau;
}





