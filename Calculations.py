

class vehicle:
    class gear:
        # Info for CTS-V T56
        qty = 6
        reverse = 2.900
        primary = 1.000
        first = 2.660
        second = 1.780
        third = 1.300
        fourth = 1.00
        fifth = 0.740
        sixth = 0.500
        final = 3.730
        reduction = final * primary
        tirediam = 26.7  # in inches
        tirerad = tirediam/2
        current = "N"
        calcedSpeed=0


    def findgear (self, RPM, Speed):
        if Speed == 0 or RPM < 1000:
            vehicle.gear.current = "N"
            return
        else:
            ratiocalcd = .00595 * RPM * vehicle.gear.tirerad / (vehicle.gear.reduction * Speed)
        firstdelta = abs(vehicle.gear.first - ratiocalcd)
        seconddelta = abs(vehicle.gear.second - ratiocalcd)
        thirddelta = abs(vehicle.gear.third - ratiocalcd)
        fourthdelta = abs(vehicle.gear.fourth - ratiocalcd)
        fifthdelta = abs(vehicle.gear.fifth - ratiocalcd)
        sixthdelta = abs(vehicle.gear.sixth - ratiocalcd)
        reversedelta = abs(vehicle.gear.reverse - ratiocalcd)
        GearArray = [firstdelta, seconddelta, thirddelta, fourthdelta, fifthdelta, sixthdelta]  # remove reverse for now
        smallestDelta = min(GearArray)
        smallestGear = GearArray.index(smallestDelta)
        if smallestGear == 6:
            vehicle.gear.current = "R"
        else:
            vehicle.gear.current = str(smallestGear + 1)




    def findspeed(self,rpm_prev,speed_prev,rpm_current):

        
        if vehicle.gear.current !="R": 
            pass
        elif vehicle.gear.current != "N":
            pass
                   
            ''' inputs: rpm at last recorded speed, previous speed, current rpm 
            output: speed at current rpm'''
   
        if rpm_prev > rpm_current:
            return speed_prev     
        else:
            return (speed_prev*rpm_current / rpm_prev)