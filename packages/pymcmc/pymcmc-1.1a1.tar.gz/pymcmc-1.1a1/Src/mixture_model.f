c ----------------------------------------------------------------------
c Fortran 77 code used in the calculation of the mixture model
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
c ----------------------------------------------------------------------
c ----------------------------------------------------------------------      

c Purpose
c =======
c
c The subroutine calcxxp is used to the outer product
c xxp(:,:,i) =  x(i,:) * x(i,:)' for i = 1, 2, ..., n,
c where x ix an (n x k) matrix of regressors.
c
c Arguments
c =========
c 
c xxp - A (k x k x n) array. On entry should be zeros.
c       On output contains the outer product
c       xxp(:,:,i) =  x(i,:) * x(i,:)',
c       for i = 1, 2, ..., n.
c
c x - An (n x k) matrix of regressors.
c
c k - An integer that denotes the number of regressors.
c      
c n - An integer that denotes the number of observations
c     in the analysis.
c
c =====================================================

      subroutine calcxxp(xxp,x,k,n)
      implicit none
      integer k,n,i
      real*8 xxp(k,k,n),x(n,k)
      real*8 alpha

      alpha=1.0

cf2py intent(inout) xxp
cf2py intent(in) x
cf2py intent(in) k
cf2py intent(in) p
      
      do i=1,n
c         outer product
          call dger(k,k,alpha,x(i,:),1,x(i,:),1,xxp(:,:,i),k)
      enddo
      end

c ----------------------------------------------------------------------
c ----------------------------------------------------------------------

c Purpose
c =======
c
c The subroutine calcxpy calculates 
c xpy = sum(x(i,:)(y(i) - alpha(index)) * s2(index))),
c where the sum is computed over i = 1, 2, ..., n. The term
c index references the component of the mixture for observation
c i.
c
c Arguments
c =========
c 
c xpy - Is a (k x 1) vector. On exit contains the computation of
c       interest.
c
c y - Is an (n x 1) vector of observations.
c      
c x - Is an (n x k) matrix of regressors.
c
c xs - Is a (k x 1) work array.
c
c a - Is an (nm x 1) vector containing the nm means of the mixture.
c
c s2 - Is an (nm x 1) vector containing the nm variances of the mixture.
c
c e - Is an (n x 1) integer vector, which specifies the component of the 
c     mixture for each observations.
c
c n - Is an integer that denotes the number of observations.
c 
c nm - Is an integer that denotes the number of components in the model.
c
c k - Is an integer that denotes the number of regressors in the model.
c      
c =====================================================


      subroutine calcxpy(xpy,y,x,xs,a,s2,e,n,nm,k)
      implicit none
      integer n,nm,k,i,j
      real*8 y(n),x(n,k),xs(k),a(nm),s2(nm),ys
      real*8 xpy(k),alpha
      integer e(n)

cf2py intent(inout) xpy
cf2py intent(in) y
cf2py intent(in) x
cf2py intent(in) xs
cf2py intent(in) a
cf2py intent(in) s2
cf2py intent(in) e
cf2py intent(in) n
cf2py intent(in) nm
cf2py intent(in) k

      alpha=1.0

c     Initialise xpy setting each element. 0.0
      do j=1,k
          xpy(j)=0.0
      enddo

      do i=1,n
          ys=(y(i)-a(e(i)+1))*s2(e(i)+1)  
          do j=1,k
              xs(j)=x(i,j)*ys
          enddo

          call daxpy(k,alpha,xs,1,xpy,1)
      enddo
      end

c ----------------------------------------------------------------------
c ----------------------------------------------------------------------

c Purpose
c =======
c
c The subroutine calcvobar computes the posterior precision for the
c regression coefficients.
c
c Arguments
c =========
c 
c vu - Is a (nr x nr) matrix that on entry contains the prior precision
c      for the regression coefficients.
c
c vo - Is a (nr x nr) matrix that on exit contains the posterior
c      precision for the regressors.
c
c xxp - Is an (nr x nr, n) array that contains the outer product
c       xxp(:,:,i) =  x(i,:) * x(i,:)',
c       for i = 1, 2, ..., n.
c
c sigj - Is an (nm x 1) vector that contains the standard deviations
c        for each component of the mixture.
c
c e - Is an (n x 1) integer vector, which specifies the component of the 
c     mixture for each observations.
c
c nr - Is an integer that denotes the number of regressors in the model.
c      
c n - Is an integer that denotes the number of observations.
c 
c nm - Is an integer that denotes the number of components in the model.
c
c =====================================================

      subroutine calcvobar(vu,vo,xxp,sigj,e,nr,n,nm)
      implicit none
      integer nr,n,i,nm,j
      real*8 vu(nr,nr),vo(nr,nr),xxp(nr,nr,n),sigj(nm)
      real*8 alpha
      integer e(n)

cf2py intent(in) vu
cf2py intent(inout) vo
cf2py intent(in) xxp
cf2py intent(in) sigj
cf2py intent(in) e
cf2py intent(in) nr
cf2py intent(in) n

      do i=1,nr
          call dcopy(nr,vu(:,i),1,vo(:,i),1)
      enddo

      do i=1,n
          alpha=sigj(e(i)+1)
          do j=1,nr
              call daxpy(nr,alpha,xxp(:,j,i),1,vo(:,j),1)
          enddo
      enddo
      end

c ----------------------------------------------------------------------
c Purpose
c =======
c
c Subroutine calculates the posterior precision for alpha
c
c Arguments
c =========
c 
c vu - Is an (nm x nm) matrix that on entry specifies the prior precision
c      matrix for alpha
c
c vo - Is an (nm x nm) matrix that on exit specifies the posterior precision
c      matrix for alpha
c
c e - Is an (n x 1) integer vector, which specifies the component of the 
c     mixture for each observations.
c
c sig - Is an (nm x 1) vector, which specifies the standard deviation
c       for each component in the mixture.
c
c nm - Is an integer that denotes the number of components in the model.
c
c n - Is an integer that denotes the number of observations.
c
c =====================================================


      subroutine calcvobara(vu,vo,e,sig,nm,n)
      implicit none
      integer nm,n,i,ind,e(n)
      real*8 vu(nm,nm),vo(nm,nm),sig(nm)

cf2py intent(in) vu
cf2py intent(inout) vo
cf2py intent(in) e
cf2py intent(in) sig
cf2py intent(in) nr
cf2py intent(in) n

      do i=1,nm
          call dcopy(nm,vu(:,i),1,vo(:,i),1)
      enddo

      do i=1,n
          ind=e(i)+1
          vo(ind,ind)=vo(ind,ind)+1.0/sig(ind)
      enddo
      end

c ----------------------------------------------------------------------

c Purpose
c =======
c
c The purpose of calcvbobara is the calculate the product
c of the posterior precision for alpha and the posterior mean
c for alpha.
c
c Arguments
c =========
c 
c vau - Is an (nm x 1) vector that on entry contains the prior precision
c       for alpha multiplied by the prior mean for alpha.
c
c vao - Is an (nm x 1) vector that on exit contains the posterior
c       precision for alpha multiplied by the posterior mean for alpha.
c
c
c sig - Is an (nm x 1) vector, which specifies the standard deviation
c       for each component in the mixture.
c
c e - Is an (n x 1) integer vector, which specifies the component of the 
c     mixture for each observations.
c
c n - Is an integer that denotes the number of observations.
c
c nm - Is an integer that denotes the number of components in the model.
c
c =====================================================

      subroutine calcvbobara(vau,vao,sig,e,y,n,nm)
      implicit none
      integer n,nm,i,e(n)
      real*8 vau(nm),vao(nm),sig(nm),y(n)

cf2py intent(in) vau
cf2py intent(inout) vao
cf2py intent(in) sig
cf2py intent(in) e
cf2py intent(in) y
cf2py intent(in) n
cf2py intent(in) nm

      call dcopy(nm,vau,1,vao,1)
      do i=1,n
          vao(e(i)+1)=vao(e(i)+1)+y(i)/sig(e(i)+1)
      enddo
      end
      
c ----------------------------------------------------------------------

c Purpose
c =======
c
c sim_evec is used to sample the an n - dimensional vector
c that is an allocation index for the mixture.
c
c Arguments
c =========
c 
c e - Is a n - dimensional integer vector. On exit it stores the
c     allocations for the mixture.
c
c ru - Is a n - dimensional vector of random uniforms.
c
c y - Is a n - dimensional vector of observations.
c
c lp - Is an (nm x n) matrix of log probabilities.
c
c al - Is an (nm x 1) vector that stores alpha.
c
c s - Is an (nm x 1) vector that stores mixture variances.
c
c p - Is an (nm, n) matrix that store pobar.
c
c pp - Is an (nm) matrix that stores p.
c
c nm - Is an integer that denotes the number of components in the
c      mixture.
c
c n - Is an integer that denotes the number of observations.
c
c =====================================================

      subroutine sim_evec(e,ru,y,lp,al,s,p,pp,nm,n)
      implicit none
      integer n,nm,i,j
      integer e(n)
      real*8 y(n),al(nm),s(nm),p(nm,n),lp(nm,n),ru(n)
      real*8 log_norm,pp(nm)

cf2py intent(inout) e
cf2py intent(in) ru
cf2py intent(in) y
cf2py intent(in) lp
cf2py intent(in) al
cf2py intent(in) s
cf2py intent(in) p
cf2py intent(in) n
cf2py intent(in) nm


c$omp parallel shared(lp,al,s,pp,p,ru,e) private(i,j)

c$omp do schedule(static)
      do i=1,n
          do j=1,nm
              lp(j,i)=log_norm(y(i),al(j),s(j)**2)+pp(j)
          enddo
 
          call calc_pe(lp,p,ru,e,i,nm,n)
      enddo
c$omp end do
c$omp end parallel
      end subroutine sim_evec
c ----------------------------------------------------------------------

c Purpose
c =======
c
c sim_evec_m is used to sample the an n - dimensional vector
c that is an allocation index for the mixture in the multivariate
c case.
c
c Arguments
c =========
c 
c e - Is a n - dimensional integer vector. On exit it stores the
c     allocations for the mixture.
c
c ru - Is a n - dimensional vector of random uniforms.
c
c y - Is a (d x n) dimensional matrix of observations.
c
c lp - Is an (nm x n) matrix of log probabilities.
c
c al - Is an (d x nm) matrix that stores mixture means.
c
c s - Is an (d x d x nm) array that stores mixture precisions.
c
c p - Is an (nm, n) matrix that store pobar.
c
c pp - Is an (nm) matrix that stores p.
c
c wk - Is an (d x 2) work matrix.
c
c lds - Is an(nm) vector of log determinates of s
c
c nm - Is an integer that denotes the number of components in the
c      mixture.
c
c n - Is an integer that denotes the number of observations.
c
c d - Is an integer that denotes the multivariate dimension.
c
c =====================================================

      subroutine sim_evec_m(e,ru,y,lp,al,s,lds,p,pp,wk,nm,n,d)
      implicit none
      integer n,nm,i,j,d
      integer e(n)
      real*8 y(d,n),al(d,nm),s(d,d,nm),p(nm,n),lp(nm,n),ru(n)
      real*8 log_normm,pp(nm),wk(d,2),lds(nm)

cf2py intent(inout) e
cf2py intent(in) ru
cf2py intent(in) y
cf2py intent(in) lp
cf2py intent(in) al
cf2py intent(in) s
cf2py intent(in) p
cf2py intent(in) n
cf2py intent(in) nm


c$omp parallel default(shared) private(i,j,wk)
c$omp do schedule(static)
      do i=1,n
          do j=1,nm
              lp(j,i)=log_normm(y(:,i),al(:,j),s(:,:,j),
     + wk,d)+pp(j)+0.5*lds(j)
          enddo
 
          call calc_pe(lp,p,ru,e,i,nm,n)
      enddo
c$omp end do
c$omp end parallel
      end subroutine sim_evec_m

c Purpose
c =======
c
c The calc_pe computes the posterior probability of
c membership to each of the k components and the 
c simulates e (indicators).
c
c Arguments
c =========
c   
c lp - Is an (nm x n) matrix of log probabilities.
c
c p - Is an (nm, n) matrix that store pobar.
c
c e - Is a n - dimensional integer vector. On exit it stores the
c     allocations for the mixture.
c
c i - Is an integer that is used to increment in loop
c
c ru - Is a n - dimensional vector of random uniforms.
c
c =====================================================

      subroutine calc_pe(lp,p,ru,e,i,nm,n)
      implicit none
      
      integer n,nm,i,j
      integer e(n)
      real*8 p(nm,n),lp(nm,n),ru(n)
      real*8 suml,sl
      integer sime
      
      sl=suml(lp(:,i),nm)
      do j=1,nm
          p(j,i)=exp(lp(j,i)-sl)
      enddo
      
      e(i)=sime(p(:,i),ru(i),nm)
      !print *, p(:,i), sum(p(:,i)), e(i)
      end subroutine calc_pe
      


c ----------------------------------------------------------------------

c Purpose
c =======
c
c sim_evec_sp is used to sample the an n - dimensional vector
c that is an allocation index for the spatial mixture.
c
c Arguments
c =========
c 
c e - Is a n - dimensional integer vector. On exit it stores the
c     allocations for the mixture.
c
c ru - Is a n - dimensional vector of random uniforms.
c
c y - Is a n - dimensional vector of observations.
c
c lp - Is an (nm x n) matrix of log probabilities.
c
c al - Is an (nm x 1) vector that stores mixture means.
c
c s - Is an (nm x 1) vector that stores the mixture variances.
c
c p - Is an (nm, n) matrix that store pobar.
c
c ne - Is an (nm, n) matrix that stores p.
c
c b - Is a spatial dependence parameter.
c
c nm - Is an integer that denotes the number of components in the
c      mixture.
c
c n - Is an integer that denotes the number of observations.
c
c =====================================================

      subroutine sim_evec_sp(e,ru,y,lp,al,s,p,ne,b,nm,n)
      implicit none
      integer n,nm,i,j
      integer e(n)
      real*8 y(n),al(nm),s(nm),p(nm,n),lp(nm,n),ru(n)
      real*8 log_norm,ne(nm,n),b

cf2py intent(inout) e
cf2py intent(in) ru
cf2py intent(in) y
cf2py intent(inout) lp
cf2py intent(in) al
cf2py intent(in) s
cf2py intent(inout) p
cf2py intent(in) ne
cf2py intent(in) b
cf2py intent(in) n
cf2py intent(in) nm


c$omp parallel shared(lp,al,s,ne,p,ru,e,b) private(i,j)

c$omp do schedule(static)
      do i=1,n
          do j=1,nm
              lp(j,i)=log_norm(y(i),al(j),s(j)**2)+b*ne(j,i)
          enddo
          
          call calc_pe(lp,p,ru,e,i,nm,n)
      enddo
c$omp end do
c$omp end parallel
      end


c ----------------------------------------------------------------------

c Purpose
c =======
c
c sim_evec_spmv is used to sample the an n - dimensional vector
c that is an allocation index for the spatial multivariate mixture.
c
c Arguments
c =========
c 
c e - Is a n - dimensional integer vector. On exit it stores the
c     allocations for the mixture.
c
c ru - Is a n - dimensional vector of random uniforms.
c
c y - Is a d x n- dimensional matrix of observations.
c
c lp - Is an (nm x n) matrix of log probabilities.
c
c al - Is an (d x nm) matrix that stores mixture means.
c
c s - Is an (d x d x nm) array that stores mixture precisions.
c
c p - Is an (nm, n) matrix that store pobar.
c
c ne - Is an (nm, n) matrix that stores current neighbour allocations.
c
c wk - Is an (d x 2) work matrix.
c
c lds - Is an (nm) vector of log determinates of s
c
c b - Is a spatial dependence parameter.
c
c nm - Is an integer that denotes the number of components in the
c      mixture.
c
c n - Is an integer that denotes the number of observations.
c
c d - Is an integer of the number variables in the multivariate mixture
c =====================================================

      subroutine sim_evec_spmv(e,ru,y,lp,al,s,p,ne,b,lds,wk,nm,n,d)
      implicit none
      integer n,nm,i,j,d,sum_b
      integer e(n)
      real*8 y(d,n),al(d,nm),s(d,d,nm),p(nm,n),lp(nm,n),ru(n)
      real*8 log_normm,ne(nm,n),b,wk(d,2),lds(nm)
      real*8 tmp(nm),tmp2

cf2py intent(inout) e
cf2py intent(in) ru
cf2py intent(in) y
cf2py intent(in) lp
cf2py intent(in) al
cf2py intent(in) s
cf2py intent(inout) p
cf2py intent(in) ne
cf2py intent(in) b
cf2py intent(in) n
cf2py intent(in) nm
cf2py intent(in) d


c$omp parallel shared(lp,al,s,ne,p,ru,e,b) private(i,j)

c$omp do schedule(static)
      
      do i=1,n
                    
          do j=1,nm
              lp(j,i)=log_normm(y(:,i),al(:,j),s(:,:,j),
     +                wk,d)+0.5*lds(j)+b*ne(j,i)
                         
          enddo
          
          call calc_pe(lp,p,ru,e,i,nm,n)
      enddo
c$omp end do
c$omp end parallel

      !print *, "Means used in sim_evec_spmv"
      !print *, n, sum(e)
      !print *, al(:,:)
      !print *, b

      end

c ----------------------------------------------------------------------

c Purpose
c =======
c
c The function sime samples from a Multinomial(1,p)
c
c Arguments
c =========
c 
c p - An (n x 1) vector of probabilites
c
c ru - A scalar that is a draw from U(0,1)
c
c n - An integer that denotes the length of p.
c
c =====================================================

      integer function sime(p,ru,n)
      implicit none
      integer n
      real*8 p(n),ru,cp
    
      cp=0.0
      sime=0
      cp=p(1)
      do while (ru.gt.cp)
          sime=sime+1
          cp=cp+p(sime+1)
      enddo
      return 
      end


c ----------------------------------------------------------------------

c Purpose
c =======
c
c The function log-norm computes the log of the normal pdf up to
c a constant. 
c
c Arguments
c =========
c 
c y - A scalar argument for the density,
c
c m - A scalar that denotes the mean of the density.
c
c ssq - A scalar denoting the variance of the density.
c
c =====================================================

      real*8 function log_norm(y,m,ssq)
      implicit none
      real*8 y,m,ssq

      log_norm=-0.5*(log(ssq)+(y-m)**2/ssq)
      return
      end

c Purpose
c =======
c
c The function log_normm computes the log of the multivariate normal
c pdf up to a constant
c
c Arguments
c =========
c 
c y - A (px1) vector
c
c =====================================================

      real*8 function log_normm(y,mean,prec,wk,p)
      implicit none
      integer p
      real*8 y(p),mean(p),prec(p,p),wk(p,2)
      real*8 alpha,beta,ddot

      !wk - y - m
      alpha=-1.0
      call dcopy(p,y,1,wk(:,1),1)
      call daxpy(p,alpha,mean,1,wk(:,1),1)
      alpha=1.0
      beta=0.0
      call dsymv('u',p,alpha,prec,p,wk(:,1),1,beta,wk(:,2),1)
      log_normm = -0.5 * ddot(p,wk(:,1),1,wk(:,2),1)
      
      return
      end function log_normm


c Purpose
c =======
c
c Function computes the log-normal distrbution
c
c Arguments
c =========
c 
c y - Is a (n x p) matrix of observations
c
c mean - Is an (p x 1) mean vector
c
c cvar - Is an (p x p) lower Cholesky triangle from the 
c        Cholesky decomposition of the variance,
c   
c wk - Is a (p x 1) work vector.
c
c p - Is the number of multivariate observations.
c
c n - Is the number of observations.
c
c =====================================================

      real*8 function log_normm_f(y, mean, cvar, wk, p, n)
      implicit none

      integer p,n,i
      real*8 y(p,n),mean(p),cvar(p,p),wk(p)
      real*8 alpha,ddot

c     compute half log determinant
      log_normm_f = 0.0
      do i=1,p
          log_normm_f = log_normm_f- log(cvar(i,i))
      enddo
      
     

      do i=1,n
          !wk - y - m
          alpha=-1.0
          call dcopy(p,y(:,i),1,wk,1)
          call daxpy(p,alpha,mean,1,wk,1)

          !wk(:,1)'inv(var)*wk(:,1)
          call dtrsv('l','n','n',p,cvar,p,wk,1)
          log_normm_f = log_normm_f -0.5 * ddot(p,wk,1, wk,1)
      enddo
      return
      end function log_normm_f
      

      



c ----------------------------------------------------------------------
c Purpose
c =======
c
c The function suml returns the log sum of an array of of logs.
c
c Arguments
c =========
c 
c lx - An (n x 1) vector of logged reals
c
c n - A integer denoting the number of logged reals.
c
c =====================================================
      
      real*8 function suml(lx,n)
      implicit none
      integer n,i
      real*8 maxl,lx(n)

      suml=0.0
      maxl=lx(1)
      do i=2,n
          if (lx(i).gt.maxl) then
              maxl=lx(i)
          endif
      enddo
        
      do i=1,n
          suml=suml+exp(lx(i)-maxl)
      enddo
      suml=log(suml)+maxl

      return
      end function suml

c ----------------------------------------------------------------------

c Purpose
c =======
c
c The subroutine neighbj computes the number of neighbouring
c  pixels that in component j, for pixel i. 
c
c Arguments
c =========
c 
c ne - Is an (nm, n) matrix.
c
c e - Is a n - dimensional integer vector. On exit it stores the
c     allocations for the mixture.
c
c nn - 
c
c indn - A (li x 1) vector of integers which is an array of 
c        neighbouring indicies stacked on top of each others. 
c        See mix_model.py for an example.
c
c b - A scalar.
c
c nm - Is an integer that denotes the number of components in the
c      mixture.
c
c n - Is an integer that denotes the number of observations.
c
c li - Is an integer that denotes the length of indn
c
c =====================================================

      subroutine  neighbj(ne,e,nn,indn,nm,n,li)
      implicit none

      integer nm,n,li,e(n),indn(li),nn(n+1)
      integer i,j,k,st,en,countj
      real*8 ne(nm,n)

cf2py intent(inout) ne
cf2py intent(in) e  
cf2py intent(in) nn
cf2py intent(in) indn
cf2py intent(in) b

c$omp parallel shared(nn,e,indn) private(i,j,st,en,countj)
c$omp do schedule(static)
      do i=1,n
          st=nn(i)
          en=nn(i+1)-1
                    
          do j=1,nm
              countj=0
              do k=st,en
	          if (e(indn(k))+1.eq.j) then
                      countj=countj+1
                  endif
              enddo
                  
              ne(j,i)=dble(countj)
          enddo
      enddo
c$omp end do
c$omp end parallel
      
      end subroutine neighbj


c ----------------------------------------------------------------------

c Purpose
c =======
c
c Function that evaluates the psuedo likelihood for the 
c spatial mixture potts model, given p and e.
c
c Arguments
c =========
c 
c ne - Is an (nm, n) matrix.
c
c e - Is a n - dimensional integer vector. On exit it stores the
c     allocations for the mixture.
c
c n - Is an integer that specifies the number of observations.
c
c k - Is an integer that specifies the number of components in the 
c     in the mixture.
c
c =====================================================


      real*8 function pseudolike(ne,e,b,n,k)
      implicit none
      integer n,k,e(n),i,j
      real*8 num,denom,tdenom,ne(k,n),b

cf2py intent(in) p
cf2py intent(in) e
cf2py intent(in) b
cf2py intent(in) n
cf2py intent(in) k


      num=0.0
      denom=0.0
c$omp parallel shared(ne,e,b) private(i,tdenom,j)
c$omp do reduction(+:num,denom)
      do i=1,n
          num=num+ne(e(i)+1,i)
          tdenom=0.0
          do j=1,k
              tdenom=tdenom+exp(b*ne(j,i))
          enddo
          denom=denom+log(tdenom)
      enddo
c$omp end parallel

      pseudolike=b*num-denom
      
      return
      end function pseudolike
            
c ----------------------------------------------------------------------
     
c Purpose
c =======
c
c The subroutine calcsobar, calculates sobar, which is one of the hyperparamters
c that describe the posterior for sigma.
c
c Arguments
c =========
c 
c rv - Is an (n x 1) work vector.
c
c y - Is the (n x 1) vector of observations. 
c
c e - Is the (n x  1) allocation vector for the mixtures.
c
c a - Is the (nm x 1) vector that provides the means for each component
c     in the mixture
c su - Is an (nm x 1) prior hyperparameter.
c
c so - Is an (nm x 1) vector that on exit is a posterior hyperameter.
c
c nm - Is an integer that defines the number of components in the
c      mixture.
c
c n - Is an integer the defines the number of observations.
c
c =====================================================

      subroutine calcsobar(rv,y,e,a,su,so,nm,n)
      implicit none
      integer nm,n,j,i,e(n)
      real*8 rv(n),y(n),su(nm),so(nm),a(nm)
      real*8 sosum

cf2py intent(in) rv
cf2py intent(in) y
cf2py intent(in) e
cf2py intent(in) a
cf2py intent(in) su
cf2py intent(inout) so
cf2py intent(in) nm
cf2py intent(in) n


c$omp parallel shared(e,y,a,su,so,rv) private(j,sosum,i)
c$omp do schedule(static)
      do i=1,n
          rv(i)=(y(i)-a(e(i)+1))**2
      enddo
c$omp end do
      
c$omp do schedule(static)
      do j=1,nm
          sosum=su(j)
          do i=1,n
              if (e(i)+1.eq.j) then
                  sosum=sosum+rv(i)
              endif
          enddo
          so(j)=sosum
      enddo
c$omp end do
c$omp end parallel

      end subroutine calcsobar


c Purpose
c =======
c
c calcsobar2 computes the scaling factor for simulating
c for the gamma distribution
c
c Arguments
c =========
c 
c y - Is an (n x 1) vector of observations.
c
c ybarj - Is an (nc x 1) vector of means for allocated y
c
c nj - Is an (nc x 1) integer vector that stores component
c      component allocation numbers
c
c e - Is the (n x  1) allocation vector for the mixtures.
c
c su - Is an (nc x 1) prior hyperparameter.
c
c so - Is an (nc x 1) vector that on exit is a posterior hyperameter.
c
c au - Is an (nc x 1) vector of hyperparmeters for component means.
c  
c mj - Is an (nc x 1) vector of hyperparameters for component mean
c     sample size.
c
c n - Is an integer that is the sample size
c
c nc - Is an integer for the number of components in the mixture
c
c =====================================================


c ---------------------------------------------------------------------
      subroutine calcsobar2(y,ybarj,nj,e,su,so,au,mj,n,nc)
      implicit none
      integer n,nc,e(n),nj(nc),j,i
      real*8 su(nc),so(nc),y(n)
      real*8 ybarj(nc),au(nc),mj(nc),sumysq,sj
      real*8 zeta

cf2py intent(in) y
cf2py intent(in) e
cf2py intent(in) su
cf2py intent(inplace) so
cf2py intent(inplace) ybarj
cf2py intent(inplace) nj
cf2py intent(in) au
cf2py intent(in) mj
cf2py intent(in) n
cf2py intent(in) nc

      do j = 1, nc
          sumysq = 0.0
          ybarj(j) = 0.0
          nj(j) = 0          

          do i = 1, n
              if (e(i)+1.eq.j) then
                  sumysq = sumysq + y(i)**2
                  ybarj(j) = ybarj(j) + y(i)
                  nj(j) = nj(j) + 1
              endif
          enddo
         
          !Note correction for the case when there is component
          !j is empty
          if (nj(j).eq.0) then
              ybarj(j) = 0.0
          else
              ybarj(j) = ybarj(j) /dble(nj(j))
          endif
          sj = sumysq - nj(j) *ybarj(j)**2
          zeta = dble(nj(j) *mj(j)) / dble(nj(j) +mj(j))
          so(j) = su(j) +sj + zeta * (ybarj(j)-au(j))**2
          
      enddo  
      !print *,ybarj
      end subroutine calcsobar2
      
     
c Purpose
c =======
c
c calcsobarm computes the scaling factor for simulating
c from the Wishart distribution.
c
c Arguments
c =========
c 
c y - Is an (d x n) matrix of observations.
c
c ybarj - Is an (d x nc) matrix of means for allocated y
c
c nj - Is an (nc x 1) integer vector that stores component
c      component allocation numbers
c
c e - Is the (n x  1) allocation vector for the mixtures.
c
c su - Is an (d x d x nc) array of prior hyperparameter.
c
c so - Is an (d x d x nc) array that on exit is a posterior hyperameter.
c
c au - Is an (d x nc) matrix of hyperparmeters for component means.
c
c sumysq - Is a (d x d) work matrix
c
c mj - Is an (nc x 1) vector of hyperparameters for component mean
c     sample size.
c
c n - Is an integer that is the sample size
c
c nc - Is an integer for the number of components in the mixture
c
c =====================================================


c ---------------------------------------------------------------------
      subroutine calcsobarm(y,ybarj,nj,e,su,so,au,sumysq,mj,n,nc,d)
      implicit none
      integer n,nc,e(n),nj(nc),j,i,k,d
      real*8 su(d,d,nc),so(d,d,nc),y(d,n)
      real*8 ybarj(d,nc),au(d,nc),mj(nc),sumysq(d,d)
      real*8 zeta,alpha

cf2py intent(in) y
cf2py intent(in) e
cf2py intent(in) su
cf2py intent(inplace) so
cf2py intent(inplace) ybarj
cf2py intent(inplace) nj
cf2py intent(in) au
cf2py intent(in) mj
cf2py intent(in) n
cf2py intent(in) nc
cf2py intent(in) d


      do j = 1, nc
          do k=1,d
              ybarj(k,j)=0.0
              do i=1,d
                  sumysq(i,k)=0.0
              enddo
          enddo
          
          nj(j) = 0          

          do i = 1, n
              if (e(i)+1.eq.j) then
                  alpha=1.0
                  !sumysq = sumysq + alpha * y(:,i) * y(:,i)'
                  call dger(d,d,alpha,y(:,i),1,y(:,i),1,sumysq,d)

                  !ybar(:,j) = y(bar(j) + alpha * (y(:,i)
                  call daxpy(d,alpha,y(:,i),1,ybarj(:,j),1)
                  nj(j) = nj(j) + 1
              endif
          enddo
    
          !print*
          !print*, "sumysq"
          !do i=1,d
          !    write(*,*) (sumysq(i,k), k=1,d)
          !enddo

          !print*
          !print*, "ybarj", ybarj(:,j)
         
          !Note correction for the case when there is component
          !j is empty
          if (nj(j).eq.0) then
              do k=1,d
                  ybarj(k,j)=0.0
              enddo
          else
              !ybarj(:,j) = ybar(:,j) / nj(j)
              alpha=1.0/dble(nj(j))
              call dscal(d,alpha,ybarj(:,j),1)
          endif
          alpha=1.0
          do k=1,d
              !so(:,k) = sumysq(:,k) 
              call dcopy(d,sumysq(:,k),1,so(:,k,j),1)
              !so = so + su
              call daxpy(d,alpha,su(:,k,j),1,so(:,k,j),1)
          enddo

          alpha=-dble(nj(j))
          !so = so -nj(j) * ybarj * ybarj'
          call dger(d,d,alpha,ybarj(:,j),1,ybarj(:,j),1,so(:,:,j),d)
          
          zeta = dble(nj(j) *mj(j)) / dble(nj(j) +mj(j))

          !Use sumysq(:,1) as work vector
          !sumysq(:,1)=ybarj(:,j)-au(:,j)
          alpha=-1.0
          call dcopy(d,ybarj(:,j),1,sumysq(:,1),1)
          call daxpy(d,alpha,au(:,j),1,sumysq(:,1),1)

          !so = so + zeta * sumysq(:,1)*sumysq(:,1)'
          call dger(d,d,zeta,sumysq(:,1),1,sumysq(:,1),1,so(:,:,j),d)
      enddo  

      end subroutine calcsobarm
      
     
c ----------------------------------------------------------------------
      
c Purpose
c =======
c
c The subroutine calcsobarr, calculates sobar for the case,
c regressors are included in the model. 
c
c Arguments
c =========
c 
c rv - Is an (n x 1) work vector.
c
c y - Is the (n x 1) vector of observations. 
c
c e - Is the (n x  1) allocation vector for the mixtures.
c
c xb - Is an (n x 1) vector that is defined by x * b, where
c      x is an (n x k) matrix of regressors and b is a (k x 1) vector
c      of regression coefficients. 
c      
c a - Is the (nm x 1) vector that provides the means for each component
c     in the mixture
c su - Is an (nm x 1) prior hyperparameter.
c
c so - Is an (nm x 1) vector that on exit is a posterior hyperameter.
c
c nm - Is an integer that defines the number of components in the
c      mixture.
c
c n - Is an integer the defines the number of observations.
c
c =====================================================

      subroutine calcsobarr(rv,y,e,xb,a,su,so,nm,n)
      implicit none
      integer nm,n,j,i,e(n)
      real*8 rv(n),y(n),su(nm),so(nm),a(nm)
      real*8 sosum,xb(n)

cf2py intent(in) rv
cf2py intent(in) y
cf2py intent(in) e
cf2py intent(in) x
cf2py intent(in) a
cf2py intent(in) su
cf2py intent(inout) so
cf2py intent(in) nm
cf2py intent(in) n


c$omp parallel shared(rv,e,y,a,su,so,xb) private(j,sosum,i)
c$omp do schedule(static)
      do i=1,n
          rv(i)=(y(i)-a(e(i)+1)-xb(i))**2
      enddo
c$omp end do

c$omp do schedule(static)
      do j=1,nm
          sosum=su(j)
          do i=1,n
              if (e(i)+1.eq.j) then
c                  rv=(y(i)-a(e(i)+1)-xb(i))**2
                  sosum=sosum+rv(i)
              endif
          enddo
          so(j)=sosum
      enddo
c$omp end do
c$omp end parallel

      end subroutine calcsobarr

c Purpose
c =======
c
c Compute the cost matrix
c
c Arguments
c =========
c 
c argument - description
c
c =====================================================

      subroutine cost_matrix(evec, cw_evec, costm, nmix, n)
      implicit none
      integer nmix, n, i, j, k
      real*8 evec(n), cw_evec(n), costm(nmix, nmix)

cf2py intent(in) evec
cf2py intent(in) cw_evec
cf2py intent(inout) costm

      do i=1,n
          do j=1,nmix
              do k=1,nmix
                  if (cw_evec(i).eq.j.and.evec(i).ne.k) then
                      costm(j,k) = costm(j,k) + 1
                  endif
              enddo
          enddo
      enddo
      end subroutine cost_matrix
      




c ----------------------------------------------------------------------

c Purpose
c =======
c
c The function num_threads returns the number of openmp threads
c
c =====================================================
!      integer function num_threads()
!      implicit none
!      integer omp_get_num_threads
!      num_threads = omp_get_num_threads()
!      return
!      end function num_threads

c ----------------------------------------------------------------------      

