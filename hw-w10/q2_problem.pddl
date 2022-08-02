(define (problem logistics2)
    (:domain logistics)

    (:objects 
        tampines - location
        changi - location
        bedok - location
        package1 - package
    )

    (:init
        (truck-at-location tampines)
        (package-at-location bedok package1)
    )

    (:goal (and
                (package-at-location changi package1)
        )
    )
)