class ParkingSystem {
public:
    int big, medium, small;
    ParkingSystem(int big, int medium, int small)
    :big(big), medium(medium), small(small)
    {
        
    }
    
    bool addCar(int carType) {
        if(carType == 1) {
            if(big>0) {
                big -= 1;
                return true;
            }
            return false;
        }
        if(carType == 2) {

            if(medium>0) {

                medium -= 1;

                return true;

            }

            return false;

        }
        if(carType == 3) {
            if(small>0) {
                small -= 1;
                return true;
            }
            return false;
        }
        return false;

    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */
