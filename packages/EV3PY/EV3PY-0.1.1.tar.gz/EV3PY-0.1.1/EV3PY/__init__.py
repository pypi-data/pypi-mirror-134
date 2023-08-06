

class MediumMotor():
    def Rotations(Port: str, Speed: float, Rotations: float, BrakeAtEnd: bool) -> str:
        if BrakeAtEnd:BaE = "Brake"
        else:BaE = "Coast"
        return("MediumMotor.Rotations MotorPort: " + Port + " | Speed: " + str(Speed) + " | Rotations: "+ str(Rotations) + " | Brake_At_End: " + str(BaE)) 

    def Degrees(Port: str, Speed: float, Degrees: float, BrakeAtEnd: bool) -> str:
        if BrakeAtEnd:BaE = "Brake"
        else:BaE = "Coast"
        return("MediumMotor.Degrees MotorPort: " + Port + " | Speed: " + str(Speed) + " | Degrees: "+ str(Degrees) + " | Brake_At_End: " + str(BaE))


    def Time(Port: str, Speed: float, Seconds: float, BrakeAtEnd: bool) -> str:
        if BrakeAtEnd:BaE = "Brake"
        else:BaE = "Coast"
        return("MediumMotor.Time MotorPort: " + Port + " | Speed: " + str(Speed) + " | Seconds: "+ str(Seconds) + " | Brake_At_End: " + str(BaE))


    def Unlimited(Port: str, Speed: float) -> str:
        return("MediumMotor.Unlimited MotorPort: " + Port + " | Speed: " + str(Speed))


    def Stop(Port: str, BrakeAtEnd: bool) -> str:
        if BrakeAtEnd:BaE = "Brake"
        else:BaE = "Coast"
        return("MediumMotor.Stop MotorPort: " + Port + " | Brake_At_End: " + str(BaE))



class GrandMotor():
    def Rotations(Port: str, Speed: float, Rotations: float, BrakeAtEnd: bool) -> str:
        if BrakeAtEnd:BaE = "Brake"
        else:BaE = "Coast"
        out = ("Motor.Rotations MotorPort: " + Port + " | Speed: " + str(Speed) + " | Rotations: "+ str(Rotations) + " | Brake_At_End: " + str(BaE))

        return out 

    def Degrees(Port: str, Speed: float, Degrees: float, BrakeAtEnd: bool) -> str:
        if BrakeAtEnd:BaE = "Brake"
        else:BaE = "Coast"
        out = ("Motor.Degrees MotorPort: " + Port + " | Speed: " + str(Speed) + " | Degrees: "+ str(Degrees) + " | Brake_At_End: " + str(BaE))

        return out


    def Time(Port: str, Speed: float, Seconds: float, BrakeAtEnd: bool) -> str:
        if BrakeAtEnd:BaE = "Brake"
        else:BaE = "Coast"
        out = ("Motor.Time MotorPort: " + Port + " | Speed: " + str(Speed) + " | Seconds: "+ str(Seconds) + " | Brake_At_End: " + str(BaE))

        return out


    def Unlimited(Port: str, Speed: float) -> str:
        out = ("Motor.Unlimited MotorPort: " + Port + " | Speed: " + str(Speed))

        return out


    def Stop(Port: str, BrakeAtEnd: bool) -> str:
        if BrakeAtEnd:BaE = "Brake"
        else:BaE = "Coast"

        out = ("Motor.Stop MotorPort: " + Port + " | Brake_At_End: " + str(BaE))

        return out


class Standard():
    def Rotations(Port: str, Speed: float, Rotations: float, BrakeAtEnd: bool) -> str:
        if BrakeAtEnd:BaE = "Brake"
        else:BaE = "Coast"
        out = ("Move.Rotations MotorPort: " + Port + " | Speed: " + str(Speed) + " | Rotations: "+ str(Rotations) + " | Brake_At_End: " + str(BaE))

        return out 

    def Degrees(Port: str, Speed: float, Degrees: float, BrakeAtEnd: bool) -> str:
        if BrakeAtEnd:BaE = "Brake"
        else:BaE = "Coast"
        out = ("Move.Degrees MotorPort: " + Port + " | Speed: " + str(Speed) + " | Degrees: "+ str(Degrees) + " | Brake_At_End: " + str(BaE))

        return out


    def Time(Port: str, Speed: float, Seconds: float, BrakeAtEnd: bool) -> str:
        if BrakeAtEnd:BaE = "Brake"
        else:BaE = "Coast"
        out = ("Move.Time MotorPort: " + Port + " | Speed: " + str(Speed) + " | Seconds: "+ str(Seconds) + " | Brake_At_End: " + str(BaE))

        return out


    def Unlimited(Port: str, Speed: float) -> str:
        out = ("Move.Unlimited MotorPort: " + Port + " | Speed: " + str(Speed))

        return out


    def Stop(Port: str, BrakeAtEnd: bool) -> str:
        if BrakeAtEnd:BaE = "Brake"
        else:BaE = "Coast"

        out = ("Move.Stop MotorPort: " + Port + " | Brake_At_End: " + str(BaE))

        return out


class Lever():
    def Rotations(LeftPort: str, RightPort: str, SpeedLeft: float, SpeedRight: float, Rotations: float, BrakeAtEnd: bool) -> str:
        if BrakeAtEnd:BaE = "Brake"
        else:BaE = "Coast"
        return(f"MoveTank.Rotations MotorPorts: {LeftPort}+{RightPort} | Speed_Left: {str(SpeedLeft)} | Speed_Right: {str(SpeedRight)} | Rotations: {str(Rotations)} | Brake_At_End: {str(BaE)}") 

    def Degrees(LeftPort: str, RightPort: str, SpeedLeft: float, SpeedRight: float, Degrees: float, BrakeAtEnd: bool) -> str:
        if BrakeAtEnd:BaE = "Brake"
        else:BaE = "Coast"
        return(f"MoveTank.Degrees MotorPorts: {LeftPort}+{RightPort} | Speed_Left: {str(SpeedLeft)} | Speed_Right: {str(SpeedRight)} | Degrees: {str(Degrees)} | Brake_At_End: {str(BaE)}")


    def Time(LeftPort: str, RightPort: str, SpeedLeft: float, SpeedRight: float, Seconds: float, BrakeAtEnd: bool) -> str:
        if BrakeAtEnd:BaE = "Brake"
        else:BaE = "Coast"
        return(f"MoveTank.Time MotorPorts: {LeftPort}+{RightPort} | Speed_Left: {str(SpeedLeft)} | Speed_Right: {str(SpeedRight)} | Seconds: {str(Seconds)} | Brake_At_End: {str(BaE)}")


    def Unlimited(LeftPort: str, RightPort: str, SpeedLeft: float, SpeedRight: float,) -> str:
        return(f"MoveTank.Unlimited MotorPorts: {LeftPort}+{RightPort} | Speed_Left: {str(SpeedLeft)} | Speed_Right: {str(SpeedRight)}")


    def Stop(LeftPort: str, RightPort: str, BrakeAtEnd: bool) -> str:
        if BrakeAtEnd:BaE = "Brake"
        else:BaE = "Coast"
        return(f"MoveTank.Stop MotorPorts: {LeftPort}+{RightPort} | Brake_At_End: {str(BaE)}")

class StartEnd():
    def Start():
        return('StartBlock')

class LoopStart():
    def Iterations(Iterations, interrupt):
        return(f"Loop(LoopCondition.Count Iterations_To_Run: {Iterations}) InterruptName: '{interrupt}'")


    def Unlimited(interrupt):
        return(f"Loop(LoopCondition.Unlimited) InterruptName: '{interrupt}'")

    def Time(Time, Interrupt):
        return(f"Loop(LoopCondition.Time How_Long: {Time}) InterruptName: '{Interrupt}'")