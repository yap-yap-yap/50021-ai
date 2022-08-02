(define (problem logistics3)
    (:domain logistics)

    (:objects 
        tampines - location
        changi - location
        bedok - location
        package1 - package
        package2 - package
    )

    (:init
        (truck-at-location tampines)
        (package-at-location bedok package1)
        (package-at-location changi package2)
    )

    (:goal (and
                (package-at-location changi package1)
                (package-at-location bedok package2)
        )
    )
)