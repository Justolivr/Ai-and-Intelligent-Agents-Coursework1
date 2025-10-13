(define (domain lunar)
    (:requirements :strips :typing)

    ; -------------------------------
    ; Types
    ; -------------------------------

    ; EXAMPLE

    ; (:types
    ;     parent_type
    ;     child_type - parent_type

    ; )
    (:types
        location
        scan picture - data
        sample rover device - object
    )

    ; samples are data are seperate


    ; -------------------------------
    ; Predicates
    ; -------------------------------

    ; EXAMPLE

    ; (:predicates
    ;     (no_arity_predicate)
    ;     (one_arity_predicate ?p - parameter_type)
    ; )

    (:predicates

        ; either true or false
        ; facts about the world

        ; an is at a certain location
        (isAt ?robject ?location)
        
        ; 2 locations are connected
        (isConnected ?location1 ?location2)

        ; it doesnt like negative preconditions so i had to define "negative" ones

        ; a rover contains data
        (hasData ?rover ?data)

        ; a rover does not contain data
        (noData ?rover ?data)

        ; a rover has a sample
        (hasSample ?rover ?sample)

        ; a rover is currently not holding a sample
        (noSample ?rover)

        ; the lander has stored a sample from the rover
        (hasStored ?lander ?data)

        ; the rover are lander are currently linked
        (isLinked ?rover ?lander)

        ; the rover has been deployed from the lander
        (isDeployed ?rover ?lander)




    )

    ; -------------------------------
    ; Actions
    ; -------------------------------

    ; rover actions

    ; lander actions
    ; land? may be a 
    ; deploy rover
    ; store rover
    ; send data

    ; EXAMPLE

    ; (:action action-template
    ;     :parameters (?p - parameter_type)
    ;     :precondition (and
    ;         (one_arity_predicate ?p)
    ;     )
    ;     :effect 
    ;     (and 
    ;         (no_arity_predicate)
    ;         (not (one_arity_predicate ?p))
    ;     )
    ; )

    ;(:action action_name
    ;    :parameters ()
    ;    :precondition (and)
    ;    :effect (and) ; pick up data
    ;)

    ;rover actions
    ; its rovering

    (:action action_name
        :parameters ()
        :precondition (and)
        :effect (and) 
    )
    

    ; drive around
    (:action moveRover
        :parameters (?rover ?lander ?startLoc ?endLoc)
        :precondition (and (isAt ?rover ?startLoc) (isConnected ?startLoc ?endLoc) (isDeployed ?rover ?lander))
        :effect (and (not (isAt ?rover ?startLoc)) (isAt ?rover ?endLoc))
    )

    ; pickup sample
    (:action pickupSample
        :parameters (?rover ?lander ?sample ?loc)
        :precondition (and (isAt ?rover ?loc) (isAt ?sample ?loc) (isDeployed ?rover ?lander) (noSample ?rover))
        :effect (and (hasSample ?rover ?sample) (not (isAt ?sample ?loc)) (not (noSample ?rover)) )
    )

    ; get a bit of data, which will be a scan or picture
    (:action getData
        :parameters (?rover ?lander ?loc ?data)
        :precondition (and (isAt ?rover ?loc) (isDeployed ?rover ?lander) (noData ?rover ?data) )
        :effect (and (hasData ?rover ?data) (not (noData ?rover ?data)) ) 
    )

    ; send some data back to the lander
     (:action sendData
        :parameters (?rover ?lander ?data)
        :precondition (and (isDeployed ?rover ?lander) (hasData ?rover ?data) (isLinked ?rover ?lander))
        :effect (and (hasStored ?lander ?data) (not(hasData ?rover ?data)) (noData ?rover ?data) ) 
    )
    


)