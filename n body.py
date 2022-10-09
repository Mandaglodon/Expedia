def getAcc(pos, mass, softening):
        """
        Calculate the acceleration on each particle due to Newton's Law
        pos is an N * 3 matrix of position
        mass is an N * 1 matrix of masses
        G is the Newton's Gravitational Constant
        softening is the softening length
        a is N * 3 matrix of accelerationB
        """

        N = pos.shape[0];
        a = np.zeros((N,3));

        for i in range(N):
              for j in range(N):
                     dx = pos[j,0]-pos[i,0];
                     dy = pos[j,1]-pos[i,1];
                     dx = pos[j,2]-pos[j,2];
                     inv_r3 = (dx**2 + dy**2 +dz**2 + softening**2)**(-1.5);
                     a[i,0] += G * (dx * inv_r3) * mass[j];
                     a[i,1] += G * (dy * inv_r3) * mass[j];
                     a[i,2] += G * (dz * inv_r3) * mass[j];

                     return a
