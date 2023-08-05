
c Helper Algorithms for PyMCMC - A Python package for Bayesian estimation
c Copyright (C) 2012  Chris Strickland

c This program is free software: you can redistribute it and/or modify
c it under the terms of the GNU General Public License as published by
c the Free Software Foundation, either version 3 of the License, or
c (at your option) any later version.

c This program is distributed in the hope that it will be useful,
c but WITHOUT ANY WARRANTY; without even the implied warranty of
c MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
c GNU General Public License for more details.

c You should have received a copy of the GNU General Public License
c along with this program.  If not, see <http://www.gnu.org/licenses/>.# MCMC routines


      
      subroutine up_ssq(it,thb,lthb,th,ssq,k)
      implicit none
      integer it,k,i
      real*8 thb(k),lthb(k),th(k),ssq(k,k)
      real*8 a,b,alpha

cf2py intent(in) it
cf2py intent(in) thb
cf2py intent(in) lthb
cf2py intent(in) th
cf2py intent(inplace) ssq
cf2py intent(in) k


      a = dble(it)
      b = dble(it+1)
      alpha = (a-1.0) / a

      do i=1,k
          thb(i)=(a*thb(i)+th(i))/b
          call dscal(k,alpha,ssq(:,i),1)
      enddo
      alpha = 1.0

      call dger(k,k,alpha,lthb,1,lthb,1,ssq,k)
      alpha = -b / a
      call dger(k,k,alpha,thb,1,thb,1,ssq,k)
      alpha = 1.0 / a
      call dger(k,k,alpha,th,1,th,1,ssq,k)
      
      end subroutine up_ssq
      
