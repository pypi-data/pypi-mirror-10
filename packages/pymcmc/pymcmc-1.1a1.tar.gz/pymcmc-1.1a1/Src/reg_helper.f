
c     Used in PyMCMC for the stochastic search algorithm.    
c     Copyright (C) 2011  Chris Strickland
c
c     This program is free software: you can redistribute it and/or modify
c     it under the terms of the GNU General Public License as published by
c     the Free Software Foundation, either version 3 of the License, or
c     (at your option) any later version.
c
c     This program is distributed in the hope that it will be useful,
c     but WITHOUT ANY WARRANTY; without even the implied warranty of
c     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
c     GNU General Public License for more details.

c     You should have received a copy of the GNU General Public License
c     along with this program.  If not, see <http://www.gnu.org/licenses/>. 

c     Fortran 77 helper functions for regtools.py

c     calculates x'x
      subroutine calcxpx(x,xpx,n,k)
      implicit none
      integer n,k
      real*8 x(n,k),xpx(k,k)
      real*8 alpha,beta

cf2py intent(in) x
cf2py intent(inplace) xpx
      
      alpha=1.0
      beta=0.0
      call dgemm('t','n',k,k,n,alpha,x,n,x,n,beta,xpx,k)
      end subroutine calcxpx

c     calculates x'y
      subroutine calcxpy(x,y,xpy,n,k)
      implicit none
      integer n,k
      real*8 x(n,k),y(n),xpy(k)
      real*8 alpha,beta

cf2py intent(in) x
cf2py intent(in) y
cf2py intent(inplace) xpy
cf2py intent(in) n
cf2py intent(in) k

      alpha=1.0
      beta=0.0

      call dgemv('t',n,k,alpha,x,n,y,1,beta,xpy,1)
      end subroutine calcxpy

c     subroutine calculates sum of squared residuals
      subroutine sumsqres(so,res,n,k)
      implicit none
      integer n,k,i
      real*8 so(k),res(n,k)
      real*8 ddot

cf2py intent(inplace) so
cf2py intent(in) res

      do i=1,k
          so(i)=so(i)+ddot(n,res(:,i),1,res(:,i),1)
      enddo
      end subroutine sumsqres
          
