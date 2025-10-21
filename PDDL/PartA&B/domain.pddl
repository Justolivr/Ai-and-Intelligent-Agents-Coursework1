(define (domain lunar)
    (:requirements :strips :typing)

    ; -------------------------------
    ; Types
    ; -------------------------------

    ; setting up types
    ; items represent "physical" objects
    ; data represents "digital" objects
    ; location is a location
    (:types
    item
    sample lander rover - item
    data
    scan pic - data
    location
    )

    ; -------------------------------
    ; Predicates
    ; -------------------------------

    ; represent facts that are true or false about the world

    (:predicates 

    ; an item is at a location
    (at ?i - item ?l1 - location)

    ; 2 locations are connected
    (connected ?l1 - location ?l2 - location)

    ; a rover has been deployed from its lander
    (deployed ?r - rover)

    ; a rover has not been deployed by its lander
    (notDeployed ?r - rover)

    ; a rover has a sample s
    (hasSample ?r - rover ?s - sample)

    ; a rover does not have a sample
    (noSample ?r - rover)

    ; a sample has been delivered to a lander
    (dropped ?s - sample)

    ; a rover has data
    (hasData ?r - rover ?d - data)
    
    ; a rover has no data
    (noData ?r - rover)

    ; a rover has uploaded data
    (uploaded ?d - data)

    ; data type to be collected a location1
    (dataAt ?d - data ?l1 - location)

    ; a lander and its location
    (landed ?l - lander ?l1 - location)
    
    ; a lander has not landed
    (notLanded ?l - lander)

    ; a rovers link to its lander
    (linked ?l - lander ?r - rover)
    )

    ; -------------------------------
    ; Actions
    ; -------------------------------

    ; move a rover from location 1 to location 2
    ; "the rover knows where it is at all times"

    ; moves the rover from a location where it is, to a location where it isnt, 
    ; and arriving at a location where it wasnt, it now is.
    ; Consequently, the location where it is, is now the location that it wasn't,
    ; and it follows that the location where it was, is now the location that it isn't


     (:action move
        :parameters (?r - rover ?l1 - location ?l2 - location)
        :precondition (and (at ?r ?l1) (connected ?l1 ?l2) (deployed ?r) )
        :effect (and (not (at ?r ?l1)) (at ?r ?l2))
    )

    ; pickup samples from a location
    (:action pickup
        :parameters (?r - rover ?s - sample ?l1 - location)
        :precondition (and (at ?r ?l1) (at ?s ?l1) (deployed ?r) (noSample ?r) )
        :effect (and (hasSample ?r ?s) (not (at ?s ?l1)) (not (noSample ?r)))
    )

    ; drop off a collected sample at its own lander
     (:action drop
        :parameters (?r - rover ?l - lander ?s - sample ?l1 - location)
        :precondition (and (at ?r ?l1) (landed ?l ?l1) (deployed ?r) (hasSample ?r ?s) (linked ?l ?r))
        :effect (and (dropped ?s) (noSample ?r))
    )

    ; deploy a rover at the location of the lander
    (:action deployRover
        :parameters (?l - lander ?r - rover ?l1 - location)
        :precondition (and (notDeployed ?r) (landed ?l ?l1)(linked ?l ?r))
        :effect (and (at ?r ?l1) (deployed ?r) (noData ?r) (noSample ?r) (not (notDeployed ?r)))
    )

    ; take a picture, or scan, depending on what is needed
    (:action getData
        :parameters (?r - rover ?d - data ?l1 - location)
        :precondition (and (at ?r ?l1) (dataAt ?d ?l1) (deployed ?r) (noData ?r))
        :effect (and (hasData ?r ?d) (not (dataAt ?d ?l1)) (not (noData ?r)))
    )

    ; send some data back to the lander
    (:action sendData
        :parameters (?r - rover ?l - lander ?d - data)
        :precondition (and (deployed ?r) (hasData ?r ?d)(linked ?l ?r))
        :effect (and (uploaded ?d)  (noData ?r) )
    )

    ; land a lander at a location
    (:action land
        :parameters (?l - lander ?r - rover ?l1 - location)
        :precondition (and (notLanded ?l) (linked ?l ?r))
        :effect (and (not (notLanded ?l)) (landed ?l ?l1) (at ?l ?l1) (notDeployed ?r) )
    )

)