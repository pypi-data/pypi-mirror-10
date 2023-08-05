c Fortran 77 code used in the Bayesian estimation of GLMs
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


c File is fortran code to assist in the estimation of the generalised
c linear model.
      
      real*8 function llink(x)
      implicit none
      real*8 x

      llink=1.0/(1.0+exp(-x))

      return
      end function llink

      real*8 function lllink(x)
      implicit none
      real*8 x,maxx

      maxx=max(0.0,x)
      lllink=x-log(exp(-maxx)+exp(x-maxx))-maxx
      return
      end function lllink

      real*8 function lomllink(x)
      implicit none
      real*8 x,maxx

      maxx=max(0.0,x)
      lomllink=-log(exp(-maxx)+exp(x-maxx))-maxx
      
      return
      end function lomllink
      

      
            
      real*8 function logl_logit(xb,y,ni,n)
      implicit none
      integer n,i
      real*8 xb(n),y(n),ni(n),lomllink,lllink

cf2py intent(in) xb
cf2py intent(in) y
cf2py intent(in) ni
cf2py intent(in) n


      logl_logit=0.0
c$omp parallel default(shared) private(i)
c$omp do reduction(+:logl_logit)
      do i=1,n
          logl_logit=logl_logit+y(i)*lllink(xb(i))+(ni(i)-y(i))*
     + lomllink(xb(i))
      enddo
c$omp end do
c$omp end parallel
      return
      end function logl_logit
       
      subroutine score(s,y,xb,x,ni,n,k)
      implicit none
      integer n,k,i,t
      real*8 y(n),x(n,k),alpha,s(k),xb(n),ni(n)
      real*8 llink, beta

cf2py intent(inout) s
cf2py intent(in) y
cf2py intent(in) xb
cf2py intent(in) ni
cf2py intent(in) x
cf2py intent(in) n
cf2py intent(in) k
    
c$omp parallel default(shared) private(t,i,beta)
      do i=1,k
c$omp single 
          alpha=0.0
c$omp end single
c$omp do reduction(+:alpha)
          do t=1,n
              beta=y(t)-ni(t)*llink(xb(t))
              alpha=alpha+beta*x(t,i)
          enddo
c$omp end do
c$omp single
          s(i)=alpha
c$omp end single
      enddo
c$omp end parallel

!      do i=1,k
!          s(i)=0.0
!      enddo
      
!      do i=1,n
!          alpha=y(i)-ni(i)*llink(xb(i))
!          call daxpy(k,alpha,x(i,:),1,s,1)
!      enddo
      end subroutine score
        
      subroutine calcxxp(xxp,x,ni,n,k)
      implicit none
      integer n,k,i
      real*8 x(n,k),xxp(k,k,n),alpha,ni(n)

cf2py intent(inout) xxp
cf2py intent(in) x  
cf2py intent(in) ni
cf2py intent(in) n
cf2py intent(in) k  

      do i=1,n
          alpha=ni(i)
          call dger(k,k,alpha,x(i,:),1,x(i,:),1,xxp(:,:,i),k)
      enddo
      
      end subroutine calcxxp
      

      subroutine hessian(h,xxp,xb,n,k)
      implicit none
      integer n,k,i,j,t
      real*8 h(k,k),xxp(k,k,n),xb(n)
      real*8 alpha,lam,llink, beta

cf2py intent(inout) h
cf2py intent(in) xxp
cf2py intent(in) xb
cf2py intent(in) n
cf2py intent(in) k
      
c$omp parallel default(shared) private(i,j,t,lam,beta)
      do i=1,k
          do j=1,k
c$omp single
              alpha=0.0
c$omp end single
c$omp do reduction(+:alpha)
              do t=1,n
                  lam=llink(xb(t))
                  beta=lam*(1.0-lam)
                  alpha=alpha+beta*xxp(j,i,t)
              enddo
c$omp end do
c$omp single
              h(j,i)=alpha
c$omp end single
          enddo
      enddo
c$omp end parallel

!      do i=1,k
!          do j=1,k
!              h(j,i)=0.0
!          enddo
!      enddo
      

!      do i=1,n
!          lam=llink(xb(i))
!          alpha=lam*(1.0-lam)
!          do j=1,k
!              call daxpy(k,alpha,xxp(:,j,i),1,h(:,j),1)
!          enddo
!      enddo
      
      end subroutine hessian

      subroutine xmbeta(xb,x,b,n,k)
      implicit none
      integer n,k
      real*8 xb(n),x(n,k),b(k),alpha,beta

      alpha=1.0
      beta=0.0
      call dgemv('n',n,k,alpha,x,n,b,1,beta,xb,1)

      end subroutine xmbeta
      
      
      subroutine lnewtonr(y,x,xb,theta,ltheta,h,xxp,s,ni,k,n)
      implicit none
      integer k,i,info,n
      real*8 x(n,k),h(k,k),s(k),xxp(k,k,n),ni(n)
      real*8 xb(n),y(n),theta(k),ltheta(k)
      real*8 diff,tol,alpha

      diff=1.0
      tol=1E-5

cf2py intent(in) y
cf2py intent(in) x
cf2py intent(in) xb
cf2py intent(in) ni
cf2py intent(inout) theta
cf2py intent(in) ltheta
cf2py intent(in) h
cf2py intent(in) xxp
cf2py intent(in) s
cf2py intent(in) k
cf2py intent(in) n


      alpha=1.0

      do while (diff.gt.tol)
          call dcopy(k,theta,1,ltheta,1)
          call xmbeta(xb,x,theta,n,k)
          call hessian(h,xxp,xb,n,k)
          call score(s,y,xb,x,ni,n,k)
          call dposv('u',k,1,h,k,s,k,info)
          call daxpy(k,alpha,s,1,theta,1)

          if (info.ne.0) then
              print *, "Warning Newton Raphson"
          endif
          
          diff=0.0
          do i=1,k
              diff=diff+(theta(i)-ltheta(i))**2
          enddo
          diff=sqrt(diff)
      enddo
          
      end subroutine lnewtonr
      
