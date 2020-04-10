class PID(object):
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.error = 0
    
    def update(self, error, dt):
        self.prev_error = self.error
        self.error = error
        self.error_sum += self.error
        self.dt = dt
        
        self.p = self.error * self.kp
        self.i = self.error_sum * self.ki
        self.d = (self.error - self.prev_error) / self.dt
        
        return self.p + self.i + self.d
        
