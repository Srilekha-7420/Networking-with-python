class Private_class_sample:
    # __tutor = None
    # __place = None
    # __experience = None
    # classvarible = "test"
    __classVaribale = "Classvariable"

    def __init__(self, tutor, place, experience):
        self.__tutor = tutor
        self.__place = place
        self.__experience = experience

    def __displayTutorDetails(self):  # private methods

        print("Tutor: {} - Place: {} - Experience: {}".format(self.__tutor, self.__place, self.__experience))

    def _displayTutorDetailsProtected(self):  # protected method
        # print("Look it won't display private methods")
        print("Tutor: {} - Place: {} - Experience: {}".format(self.__tutor, self.__place, self.__experience))
        return self.__tutor, self.__place

    def displayTutorDetailsPublic(self):
        print(Private_class_sample.__classVaribale)
        print("Tutor: {} - Place: {} - Experience: {}".format(self.__tutor, self.__place, self.__experience))
        self.__displayTutorDetails()
    def returnPrivateVariable(self):
        return Private_class_sample.__classVaribale


class Derived_Private_Class(Private_class_sample):
    def display_parent_private_method(self):
        self.__displayTutorDetails()

    def display_parent_protected_method(self):
        tutor, place = self._displayTutorDetailsProtected()
        print(tutor, place)

    def display_parent_public_method(self):
        self.displayTutorDetailsPublic()

    def getprivatevalue(self):
        val = self.returnPrivateVariable()
        print("======")
        print(val)


derivedPrivateObj = Derived_Private_Class("Shree", "Vijayawada", 5)
# derivedPrivateObj.display_parent_private_method()
derivedPrivateObj.display_parent_protected_method()
derivedPrivateObj.display_parent_public_method()
derivedPrivateObj.getprivatevalue()


class Private_class_sample:
    # __tutor = None
    # __place = None
    # __experience = None
    # classvarible = "test"

    def __init__(self, tutor, place, experience):
        self.__tutor = tutor
        self.__place = place
        self.__experience = experience

    def display(self):
        print(self.__tutor)

derivedPrivateObj = Private_class_sample("Shree", "Vijayawada", 5)
derivedPrivateObj.display()