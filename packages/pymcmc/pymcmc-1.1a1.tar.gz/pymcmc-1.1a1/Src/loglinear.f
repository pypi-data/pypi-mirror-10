c Fortran 77 code used in the Bayesian estimation of the loglinear
c model.
c Copyright (C) 2011  Chris Strickland

c This program is free software: you can redistribute it and/or modify
c it under the terms of the GNU General Public License as published by
c the Free Software Foundation, either version 3 of the License, or
c (at your option) any later version.

c This program is distributed in the hope that it will be useful,
c but WITHOUT ANY WARRANTY; without even the implied warranty of
c MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
c GNU General Public License for more details.

c You should have received a copy of the GNU General Public License
c along with this program.  If not, see <http://www.gnu.org/licenses/>.


c     Fortran 77 code for the log linear model


c Purpose
c =======
c
c Function calculates the log like-lihood function for the
c log linear model up to a constant of proportionality. Specifically
c the log likelihood is calculate as
c
c ln L = Sum_i(-exp(xb(i)) + y(i) * xb(i)). Note that in the Python
c code that calls this function the integrating constant -Sum_i(log(y(i)!))
c is added 
c
c Arguments
c =========
c 
c y - Is the (n x 1) vector of observations y.
c
c xb - Is the (n x 1) vector that is constructed by dot(x, b), where
c      x is an (n x k) matrix of regressors and b is a (k x 1) vector
c      of regression coefficients.
c
c n - Is an integer that defines the number of observations.
c
c =====================================================

      real*8 function logl(xb,y,n)
      implicit none
      integer n,i
      real*8 xb(n),y(n)

cf2py intent(in) xb
cf2py intent(in) y
cf2py intent(in) n

      logl=0.0
c$omp parallel shared(xb,y)
c$omp do reduction(+:logl)
      do i=1,n
          logl=logl+y(i)*xb(i)-exp(xb(i))
      enddo
c$omp end parallel
      return
      end function logl

c Purpose
c =======
c
c The subroutine score returns the score vector.
c
c Arguments
c =========
c 
c s - Is the (k x 1) score vector.
c
c y - Is the (n x 1) vector of observations y.
c
c xb - Is the (n x 1) vector that is constructed by dot(x, b), where
c      x is an (n x k) matrix of regressors and b is a (k x 1) vector
c      of regression coefficients.
c
c x - Is an (n x k) matrix of regressors.
c
c n - Is an integer that defines the number of observations.
c
c k - Is an integer that defines the number of regressors.
c =====================================================


      
      subroutine score(s,y,xb,x,n,k)
      implicit none
      integer n,k,i,t
      real*8 xb(n),x(n,k),s(k),y(n)
      real*8 alpha

cf2py intent(inout) s
cf2py intent(in) y
cf2py intent(in) xb
cf2py intent(in) x
cf2py intent(in) n
cf2py intent(in) k

      
c$omp parallel default(shared) private(t,i)
      do i=1,k
c$omp single 
          alpha=0.0
c$omp end single
c$omp do reduction(+:alpha)
          do t=1,n
              alpha=alpha+(y(t)-exp(xb(t)))*x(t,i)
          enddo
c$omp end do
c$omp single
          s(i)=alpha
c$omp end single
      enddo
c$omp end parallel

c Sequential Implementation
c      do i=1,k
c          s(i)=0.0
c      enddo

c      do i=1,n
c          alpha=y(i)-exp(xb(i))
c          call daxpy(k,alpha,x(i,:),1,s,1)
c      enddo
      end subroutine score
      
c Purpose
c =======
c
c The subroutine calcxxp calculates the outer products
c x(i)x(i)' for i = 1,2,...,n. The result is stored in the
c array xxp.
c
c Arguments
c =========
c 
c xxp - Is a (k x k x n) array that stores the outer products
c x(i)x(i)' for i = 1,2,...,n.
c
c x - Is an (n x k) matrix of regressors.
c
c n - Is an integer that denotes the number of observations.
c
c k - Is an integer that denotes the number of regressors.
c
c =====================================================

          
      subroutine calcxxp(xxp,x,n,k)
      implicit none
      integer n,k,i
      real*8 x(n,k),xxp(k,k,n),alpha

      alpha=1.0

      do i=1,n
          call dger(k,k,alpha,x(i,:),1,x(i,:),1,xxp(:,:,i),k)
      enddo
      
      end subroutine calcxxp

c Purpose
c =======
c
c The subroutine hessian calculates the hessian.
c
c Arguments
c =========
c 
c h - Is a (k x k) matrix that stores the hessian.
c
c xxp - Is a (k x k x n) array that stores the outer products
c x(i)x(i)' for i = 1,2,...,n.
c
c xb - Is the (n x 1) vector that is constructed by dot(x, b), where
c      x is an (n x k) matrix of regressors and b is a (k x 1) vector
c      of regression coefficients.
c
c n - Is an integer that denotes the number of observations.
c
c k - Is an integer that denotes the number of regressors.
c
c =====================================================


      subroutine hessian(h,xxp,xb,n,k)
      implicit none
      integer n,k,i,j,t
      integer seq
      real*8 h(k,k),xxp(k,k,n),xb(n)
      real*8 alpha

cf2py intent(inout) h
cf2py intent(in) xxp
cf2py intent(in) xb
cf2py intent(in) n
cf2py intent(in) k

      
    
c$omp parallel default(shared) private(i,j,t)
      do i=1,k
          do j=1,k
c$omp single
              alpha=0.0
c$omp end single
c$omp do reduction(+:alpha)
              do t=1,n
                  alpha=alpha+exp(xb(t))*xxp(j,i,t)
              enddo
c$omp end do
c$omp single
              h(j,i)=alpha
c$omp end single
          enddo
      enddo
c$omp end parallel
      
c Sequential version
c      do i=1,k
c          do j=1,k
c              h(j,i)=0.0
c          enddo
c      enddo

c      do i=1,n
c          alpha=exp(xb(i))
c          do j=1,k
c              call daxpy(k,alpha,xxp(:,j,i),1,h(:,j),1)
c          enddo
c      enddo
      
      end subroutine hessian
      
      subroutine xmbeta(xb,x,b,n,k)
      implicit none
      integer n,k
      real*8 xb(n),x(n,k),b(k),alpha,beta

      alpha=1.0
      beta=0.0
      call dgemv('n',n,k,alpha,x,n,b,1,beta,xb,1)

      end subroutine xmbeta

      subroutine newtonr(y,x,xb,theta,ltheta,h,xxp,s,ipiv,wk,lwk,k,n)
      implicit none
      integer k,i,j,info,n,ipiv(k),fl,lwk
      real*8 x(n,k),h(k,k),s(k),xxp(k,k,n)
      real*8 xb(n),y(n),theta(k),ltheta(k)
      real*8 diff,tol,alpha,wk(lwk)

      diff=1.0
      tol=1E-5

cf2py intent(in) y
cf2py intent(in) x
cf2py intent(in) xb
cf2py intent(inout) theta
cf2py intent(in) ltheta
cf2py intent(in) h
cf2py intent(in) xxp
cf2py intent(in) s
cf2py intent(in) ipiv
cf2py intent(in) wk
cf2py intent(in) lwk
cf2py intent(in) k
cf2py intent(in) n


      alpha=1.0
      fl=0

      do while (diff.gt.tol)
          call dcopy(k,theta,1,ltheta,1)
          call xmbeta(xb,x,theta,n,k)
          call hessian(h,xxp,xb,n,k)
          call score(s,y,xb,x,n,k)
          call dposv('u',k,1,h,k,s,k,info)
          if (info.ne.0.or.fl.eq.1) then
              !call hessian(h,xxp,xb,n,k)
              !call score(s,y,xb,x,n,k)
              !call dsysv('u',k,1,h,k,ipiv,s,k,wk,lwk,info)
              !fl=1
              print *, "Warning Newton Raphson"
          endif

          call daxpy(k,alpha,s,1,theta,1)

          
          diff=0.0
          do i=1,k
              diff=diff+(theta(i)-ltheta(i))**2
          enddo
          diff=sqrt(diff)
      enddo
          
      end subroutine newtonr
     
c Purpose
c =======
c
c The function intconst works out the integrating constant for the
c likeihood of the log-linear model. Specifically the function returns
c intconst = Sum_i(log(y(i)!))
c
c Arguments
c =========
c          
c y - Is an (n x 1) vector of observations.
c
c n - Is an integer that defines the number of observations.
c
c =====================================================
 
      real*8 function intconst(y,n)
      implicit none
      integer n,i
      real*8 y(n),lgama

cf2py intent(in) y
cf2py intent(in) n


      intconst=0.0
c$omp parallel shared(y)
c$omp do reduction(+:intconst)
      do i=1,n
          intconst=intconst-lgama(y(i)+1)
      enddo
c$omp end parallel
      return
      end function intconst
      
