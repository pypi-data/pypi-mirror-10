c Fortran 77 source code for the Python library PySSM
c Copyright (C) 2010  Chris Strickland

c This program is free software: you can redistribute it and/or modify
c it under the terms of the GNU General Public License as published by
c the Free Software Foundation, either version 2 or verion 3 of the
c License.

c This program is distributed in the hope that it will be useful,
c but WITHOUT ANY WARRANTY; without even the implied warranty of
c MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
c GNU General Public License for more details.

c You should have received a copy of the GNU General Public License
c along with this program.  If not, see <http://www.gnu.org/licenses/>.


c ------------------------------------------------------------------
c Filtering and smoothing code with regressors + associated functions
c ------------------------------------------------------------------

c     Procedure determines index of time varying system matrix       
      integer function timet(n, t)
      implicit none
      integer n, t
c     Choose t th matrix or first. n > 1 => time varying
      timet = 1
      if(n.gt.1) then 
          timet = t      
      endif     
      return 
      end function timet

c ---------------------------------------------------------------------

c **/** NEW OPENMP ADDED - UNTESTED **/**
      
c     simulates data for standard state space model 
      subroutine srsimssm(y, zt, ch, tt, cqt, rvm, rvs, av, wb, n,
     + r, p, m, n_z, n_h, n_t, n_q, p1)
      integer n, r, p, m, t, t_z, t_h, t_t, t_q, p1, i
      integer n_z, n_h, n_t, n_q, timet
      real*8 y(p,n), zt(p,m,n_z), ch(p,p1,n_h), tt(m,m,n_t)
      real*8 rvm(p,n), rvs(r,n), av(m,n), cqt(m,r,n_q), wb(m,n)
      real*8 alpha, beta

c     cqt is the cholesky decomposition of qt
c     cht is the sqrt of the ht. recall that ht is a vector
c ---------------------
cf2py intent(inout) y
cf2py intent(in) zt
cf2py intent(in) ch
cf2py intent(in) tt
cf2py intent(in) cqt
cf2py intent(in) rvm
cf2py intent(in) rvs
cf2py intent(inout) av
cf2py intent(in) wb
cf2py intent(in) n
cf2py intent(in) r
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n_z
cf2py intent(in) n_h
cf2py intent(in) n_t
cf2py intent(in) n_q
c ------------------
      alpha = 1.0
      beta = 1.0
      
c$omp parallel default(shared)       
c$omp do schedule(static) private(t, t_q)
      do t = 1, n-1          
                                          
c         Initialise: av(t+1) = wb(t)                                          
          call dcopy(m, wb(:,t), 1, av(:,t+1), 1)

c         Compute: av(t+1) = av(t+1) + cqt(t) * rvc(t)          
          t_q = timet(n_q, t)
          call dgemv('n',m,r,alpha,cqt(:,:,t_q),m,rvs(:,t),1,beta,
     + av(:,t+1),1)     
      enddo
c$omp end do    

c$omp single     
      do t = 1, n-1     
c         Compute: av(t+1) = av(t+1) + tt(t) * av(t)      
          t_t = timet(n_t, t)
          call dgemv('n',m,m,alpha,tt(:,:,t_t),m,av(:,t),1,beta,
     + av(:,t+1),1)
      enddo
c$omp end single      
      
c$omp do schedule(static) private(t, t_h, t_z, beta, i)
      do t = 1, n
      
          t_h = timet(n_h, t)
          t_z = timet(n_z, t)
          
c         Compute: y(t) = ch(t) * rvm(t)          
          beta = 0.0
          if (p1.eq.p) then
              call dgemv('n',p,p,alpha,ch(:,:,t_h),p,rvm(:,t),1,beta,
     +             y(:,t),1)
          else
              do i=1,p
                  y(i,t) = ch(i,1,t_h) * rvm(i,t)
              enddo
          endif
              

     
c         Compute: y(t) = y(t) + zt(t) * av(t)
          beta = 1.0
          call dgemv('n',p,m,alpha,zt(:,:,t_z),p,av(:,t),1, beta,
     + y(:,t),1)
      enddo
c$omp end do
c$omp end parallel

      end

c ---------------------------------------------------------------------

c **/** NEW OPENMP ADDED - UNTESTED **/**

c     non time varying version that simulates data with state regressors     
      subroutine ntsrsimssm(y,zt,ch,tt,cqt,rvm,rvs,av,wb,n,r,p,p1,m)
      integer n,p,m,r,t,p1,i
      real*8 y(p,n), zt(p,m), ch(p,p1), tt(m,m), wb(m,n)
      real*8 rvm(p,n),rvs(r,n), av(m,n), cqt(m,r)
      real*8 alpha, beta

c     cqt is the cholesky decomposition of qt
c     cht is the sqrt of the ht. recall that ht is a vector
c ----------------------
cf2py intent(inout) y
cf2py intent(in) zt
cf2py intent(in) ch
cf2py intent(in) tt
cf2py intent(in) cqt
cf2py intent(in) rvm
cf2py intent(in) rvs
cf2py intent(inout) av
cf2py intent(inout) wb
cf2py intent(in) n
cf2py intent(in) r
cf2py intent(in) p
cf2py intent(in) p1
cf2py intent(in) m
c --------------------
      alpha = 1.0
      beta = 1.0

c$omp parallel default(shared) private(t)       
c$omp do schedule(static)       
      do t = 1, n-1     

c         Initialise: av(t+1) = wb(t)       
          call dcopy(m,wb(:,t),1,av(:,t+1),1)
          
c         Compute: av(t+1) = av(t+1) + cqt * rvs(t)          
          call dgemv('n',m,r,alpha,cqt,m,rvs(:,t),1,beta,
     + av(:,t+1),1)
      enddo
c$omp end do      
c$omp end parallel     

      do t = 1, n-1      
c         Compute: av(t+1) += tt * av(t)       
          call dgemv('n',m,m,alpha,tt,m,av(:,t),1,beta,
     + av(:,t+1),1)     
      enddo

      beta = 0.0
      if (p1.eq.p) then
          call dgemm('n','n',p,n,p,alpha,ch,p,rvm,p,beta,y,p)
      else
c$omp parallel default(shared) private(t,i)       
c$omp do schedule(static)       
          do t=1,n
              do i=1,p
                  y(i,t)=ch(i,1)*rvm(i,t)
              enddo
          enddo
      endif
c$omp end do      
c$omp end parallel     
              
      beta = 1.0
      call dgemm('n','n',p,n,m,alpha,zt,p,av,m,beta,y,p)
      end

c ---------------------------------------------------------------------

c     subroutine for filtering with the standard state SSM, regressors
c     in the state equation
      subroutine srfilter(y,z,h,tt,qt,nu,k,f,s,a,at,pt,ps,mt,w,ls,lk,
     + ilike,ifo,wb,pmiss, wk, m,p,p1, n, n_z, n_h, n_t, n_q)
      integer m,p,n,t,i,ifo,info,ilike, t_z, t_h, t_t, t_q,j
      integer n_z, n_h, n_t, n_q, timet, p1, pmiss(n)
      real*8 y(p,n), z(p,m,n_z), h(p,p1,n_h), tt(m,m,n_t), qt(m,m,n_q)
      real*8 nu(p,n), k(m,p,n), s(p,m,n), ls(m,m,n), a(m,n)
      real*8 ps(m,m,n), mt(m,p), at(m), pt(m,m), f(p,p), w(m,m)
      real*8 alpha, beta,lk(1), logdet,ddot, llike,wb(m,n),wk(p)
c --------------------
cf2py intent(in) y
cf2py intent(in) z
cf2py intent(in) h
cf2py intent(in) tt
cf2py intent(in) qt
cf2py intent(inout) nu
cf2py intent(inout) k
cf2py intent(in) f
cf2py intent(inout) s
cf2py intent(inout) a
cf2py intent(in) at
cf2py intent(in) pt
cf2py intent(inout) ps
cf2py intent(in) mt
cf2py intent(in) w
cf2py intent(in) ilike
cf2py intent(inplace) lk
cf2py intent(inout) wb
cf2py intent(inout) ifo
cf2py intent(in) m
cf2py intent(in) p
cf2py intent(in) p1
cf2py intent(in) n
cf2py intent(in) n_z
cf2py intent(in) n_h
cf2py intent(in) n_t
cf2py intent(in) n_q
c --------------------
c     note if lk.lt.-1 then calculate likelihood and return in lk(1)

      ifo = 0
      llike = 0.0

      do t = 1, n
      
          t_t = timet(n_t, t)          
          t_z = timet(n_z, t)
          t_h = timet(n_h, t)
          t_q = timet(n_q, t)
      
          call dcopy(m,at,1,a(:,t),1)
          do i=1,m
              call dcopy(m,pt(:,i),1,ps(:,i,t),1)
          enddo

c         Compute: Nu(t)= Y(t) - Z(t)*a(t)     
          call dcopy(p,y(:,t),1,nu(:,t),1)
          alpha=-1.0
          beta=1.0
          call dgemv('n',p,m,alpha,z(:,:,t_z),p,at,1,beta,nu(:,t),1)

c         Compute: m(t) = P(t)*Z(t)' 
c         Use k(:,:,t) as workspace to store Z(t)'
          
          do i=1,m
              do j=1,p
                  k(i,j,t) = z(j,i,t_z)
              enddo
          enddo

          alpha=1.0
          beta=0.0         
          call dsymm('l','u',m,p,alpha,pt,m,k(:,:,t),m,beta,mt,m)
          
          !call dgemm('n','t',m,p,m,alpha,pt,m,z(:,:,t_z),p,beta,mt,m)

          if (pmiss(t).eq.0) then
c             Compute: F(t) = Z(t)*m(t)+H(t)          
              if (p.eq.p1) then
                  do i=1,p
                      call dcopy(p,h(:,i,t_h),1,f(:,i),1)
                  enddo
                  beta=1.0
                  call dgemm('n','n',p,p,m,alpha,z(:,:,t_z),p,mt,m,
     + beta,f,p)
              else
                  call dgemm('n','n',p,p,m,alpha,z(:,:,t_z),p,mt,m, 
     + beta,f,p)
                  do i=1,p
                      f(i,i)=f(i,i)+h(i,1,t_h)
                  enddo
              endif


              
c             Compute: F(t)*S(t) = Z(t); solve for S(t)=inv(F(t))*Z(t)         
              do i=1,m
                  call dcopy(p,z(:,i,t_z),1,s(:,i,t),1)
              enddo
              call dposv('u',p,m,f,p,s(:,:,t),p,info)
              if (info.ne.0) then
                  ifo=1
              endif
              beta=0.0
c         if lk(1).lt.-1 then calculate log-likelihood
              if (ilike.eq.0) then
                  logdet=0.0
                  do i=1,p
                      logdet=logdet+2.0*log(f(i,i))
                  enddo
                  call dcopy(p,nu(:,t),1,wk,1)
                  call dtrsm('l','u','t','n',p,1,alpha,f,p,wk,p)
                  call dtrsm('l','u','n','n',p,1,alpha,f,p,wk,p)
                  llike=llike-0.5*(logdet+ddot(p,wk,1,nu(:,t),1))

              endif

          
c             Compute: W(t) = T(t)*P(t)


              call dsymm('r','u',m,m,alpha,pt,m,tt(:,:,t_t),m,beta,
     + w,m)
               

              !call dgemm('n','n',m,m,m,alpha,tt(:,:,t_t),m,pt,m,beta,
!     + w,m)

c             Compute: K(t) = W(t)*S(t)'
              call dgemm('n','t',m,p,m,alpha,w,m,s(:,:,t),p,beta,
     + k(:,:,t),m)

c             Compute: L(t)=T(t)-K(t)*Z(t)
              do i=1,m
                  call dcopy(m,tt(:,i,t_t),1,ls(:,i,t),1)
              enddo
              alpha=-1.0
              beta=1.0
              call dgemm('n','n',m,m,p,alpha,k(:,:,t),m,z(:,:,t_z),
     + p,beta,ls(:,:,t),m)

              alpha=1.0
              beta=0.0
              
c             Compute: a(t+1) = wb(t)+T(t)*a(t)+K(t)*nu(t)
              call dgemv('n',m,m,alpha,tt(:,:,t_t),m,a(:,t),1,beta,at,1)
              beta=1.0
              call dgemv('n',m,p,alpha,k(:,:,t),m,nu(:,t),1,beta,at,1)
              beta=0.0
              call daxpy(m,alpha,wb(:,t),1,at,1)

c             Compute: P(t+1) = W(t)*L(t)'+Q(t)
c             call dgemm('n','n',m,m,m,alpha,tt(:,:,t),m,pt,m,beta,w,m)
              do i=1,m
                  call dcopy(m,qt(:,i,t_q),1,pt(:,i),1)
              enddo
              beta=1.0
              call dgemm('n','t',m,m,m,alpha,w,m,ls(:,:,t),m,beta,pt,m)
          else
c             Compute: a(t+1) = wb(t)+T(t)*a(t)
              call dgemv('n',m,m,alpha,tt(:,:,t_t),m,a(:,t),1,beta,at,1)
              beta=0.0
              call daxpy(m,alpha,wb(:,t),1,at,1)
c             Compute: P(t+1) = W(t)*L(t)'+Q(t)
              call dgemm('n','n',m,m,m,alpha,tt(:,:,t),m,pt,m,beta,w,m)
              do i=1,m
                  call dcopy(m,qt(:,i,t_q),1,pt(:,i),1)
              enddo
              beta=1.0
              call dgemm('n','t',m,m,m,alpha,w,m,tt(:,:,t_t),m,beta,
     + pt,m)
          endif

      enddo
      lk(1)=llike
      end
c ----------------------------------------------------------------------

c     subroutine for filtering with the standard state SSM, regressors
c     in the state equation. Diffuse kalman filter.

      subroutine srdfilter(y,z,h,tt,qt,nu,ks,f,s,at,pt,mt,w,ls,
     + ifo,wbb,xbb,ttat,qm,wnu,lk,ilike,m,p,n,k1,k2,k3, n_z, n_h, n_t,
     +  n_q, p1)
      integer m,p,n,t,i,j,k,ifo, info,k1,k2, k3, t_z, t_h, t_t, t_q
      integer n_z, n_h, n_t, n_q, timet,ilike, p1
      real*8 y(p,n), z(p,m,n_z), h(p,p1,n_h), tt(m,m,n_t), qt(m,m,n_q)
      real*8 nu(p,k3,n), ks(m,p,n), s(p,m,n), ls(m,m,n)
      real*8 mt(m,p), at(m,k2), pt(m,m), f(p,p), w(m,m)
      real*8 alpha,beta, wbb(m,k2,n), qm(k3,k3)
      real*8 xbb(p,k1,n), ttat(m,k2), wnu(p,k2)
      real*8 lk(*),llike
c --------------------
cf2py intent(in) y
cf2py intent(in) z
cf2py intent(in) h
cf2py intent(in) tt
cf2py intent(in) qt
cf2py intent(inout) nu
cf2py intent(inout) ks
cf2py intent(in) f
cf2py intent(inout) s
cf2py intent(in) at
cf2py intent(in) pt
cf2py intent(in) mt
cf2py intent(in) w
cf2py intent(in) wbb
cf2py intent(inout) ifo
cf2py intent(in) xbb
cf2py intent(in) ttat
cf2py intent(inout) qm
cf2py intent(inout) lk
cf2py intent(in) wnu
cf2py intent(in) m
cf2py intent(in) p
cf2py intent(in) p1
cf2py intent(in) n
cf2py intent(in) k
cf2py intent(in) n_z
cf2py intent(in) n_h
cf2py intent(in) n_t
cf2py intent(in) n_q
c -------------------

      llike=0.0

      k=k3-1
      ifo = 0
      do i = 1, k+1
          do j = 1, k+1
              qm(i,j) = 0.0
          enddo
      enddo

      do t = 1, n
      
          t_z = timet(n_z, t)
          t_h = timet(n_h, t)
          t_t = timet(n_t, t)
          t_q = timet(n_q, t)
      
c         Compute: Nu(t)= [0,Y(y)] - X(t)Bb - Z(t)A(t)
          do j = 1, k
              do i = 1, p
                  nu(i,j,t) = 0.0
              enddo
          enddo
          
          call dcopy(p,y(:,t),1,nu(:,k+1,t),1)
          
          alpha = -1.0
          beta = 1.0
              
          call dgemm('n','n', p, k+1, m, alpha, z(:,:,t_z), p, at, 
     + m,beta,nu(:,:,t),p)                
          
          if (k1.ne.0) then
              do j = 1, k+1
                  call daxpy(p,alpha,xbb(:,j,t),1,nu(:,j,t),1)
              enddo
          endif
          
          alpha = 1.0
          beta = 0.0
          
c         Compute: m(t) = P(t)*Z(t)'          
          call dgemm('n','t',m,p,m,alpha,pt,m,z(:,:,t_z),p,beta,mt,m)

c         Compute: F(t) = Z(t)*m(t)+H(t)                    
          if (p1.eq.p) then
              do i = 1, p
                  call dcopy(p,h(:,i,t_h),1,f(:,i),1)
              enddo
              
              beta = 1.0
              call dgemm('n','n',p,p,m,alpha,z(:,:,t_z),p,mt,m,beta,f,p)
          else
              call dgemm('n','n',p,p,m,alpha,z(:,:,t_z),p,mt,m,beta,f,p)
              do i=1,p
                  f(i,i) = f(i,i) + h(i,1,t_h)
              enddo
          endif
              

c         Compute: F(t)*S(t) = Z(t); solve for S(t) = inv(F(t))*Z(t)          
          do i = 1,m
              call dcopy(p,z(:,i,t_z),1,s(:,i,t),1)
          enddo
          call dposv('u',p,m,f,p,s(:,:,t),p,info)
          if (info.ne.0) then
              ifo=1
          endif

          
          if (ilike.eq.0) then
              do i = 1, p
                llike = llike - log(f(i,i))
              enddo
          endif

          
c         Compute: Qm(t) = Qm(t) + Nu(t)'*inv(F(t))*Nu(t)          
          do j = 1,k+1
              call dcopy(p,nu(:,j,t),1,wnu(:,j),1)
          enddo

          call dtrsm('l','u','t','n',p,k+1,alpha,f,p,wnu,p)
          beta = 1.0
          call dgemm('t','n',k+1,k+1,p,alpha,wnu,p,wnu,p,
     + beta,qm,k+1)

          beta=0.0
          
c         Compute: W(t) = T(t)*P(t)
          call dgemm('n','n',m,m,m,alpha,tt(:,:,t_t),m,pt,m,beta,w,m)

c         Compute: K(t) = W(t)*S(t)'
          call dgemm('n','t',m,p,m,alpha,w,m,s(:,:,t),p,beta,ks(:,:,t),
     + m)
     
c         Compute: L(t) = T(t)- K(t)*Z(t)
          do i=1,m
              call dcopy(m,tt(:,i,t_t),1,ls(:,i,t),1)
          enddo
          alpha = -1.0
          beta = 1.0
          call dgemm('n','n',m,m,p,alpha,ks(:,:,t),m,z(:,:,t_z),p,beta,
     + ls(:,:,t),m)

          alpha = 1.0
          beta = 0.0
          
c        Compute: a(t+1) = wbb(t) + T(t)*a(t) + K(t)*nu(t)

          call dgemm('n','n', m, k+1, m, alpha, tt(:,:,t_t), m,
     + at,m,beta,ttat,m)
          do j= 1, k+1
              call dcopy(m,ttat(:,j),1,at(:,j),1)
          enddo
          beta = 1.0
          call dgemm('n','n', m, k+1, p, alpha, ks(:,:,t), m, 
     + nu(:,:,t), p, beta, at, m)
          if (k2.ne.0) then
              do j = 1, k+1
                  call daxpy(m,beta,wbb(:,j,t),1,at(:,j),1)
              enddo
          endif
          
c         Compute: P(t+1) = W(t)*L(t)' + Q(t)
c          call dgemm('n','n',m,m,m,alpha,tt(:,:,t),m,pt,m,beta,w,m)
          do i = 1,m
              call dcopy(m,qt(:,i,t_q),1,pt(:,i),1)
          enddo
          beta = 1.0
          call dgemm('n','t',m,m,m,alpha,w,m,ls(:,:,t),m,beta,pt,m)
      enddo
      lk(1)=llike
      end
c ----------------------------------------------------------------------

c     subroutine for filtering with the standard state SSM, regressors
c     in the state equation. Diffuse kalman filter.
      subroutine srdntfilter(y,z,h,tt,qt,nu,ks,f,s,at,pt,mt,w,ls,
     + ifo,wbb,xbb,ttat,qm,wnu,lk,ilike,m,p,p1,n,k1,k2,k3)
      integer m,p,n,t,i,j,ifo,info,k,k2,ilike,p1
      real*8 y(p,n), z(p,m), h(p,p1), tt(m,m), qt(m,m)
      real*8 nu(p,k3,n), ks(m,p,n), s(p,m,n), ls(m,m,n)
      real*8 mt(m,p), at(m,k2), pt(m,m), f(p,p), w(m,m)
      real*8 alpha, beta, wbb(m,k2,n), qm(k3,k3)
      real*8 xbb(p,k1,n), ttat(m,k2), wnu(p,k2),lk(*),llike
c ------------------
cf2py intent(in) y
cf2py intent(in) z
cf2py intent(in) h
cf2py intent(in) tt
cf2py intent(in) qt
cf2py intent(inout) nu
cf2py intent(inout) ks
cf2py intent(in) f
cf2py intent(inout) s
cf2py intent(in) at
cf2py intent(in) pt
cf2py intent(in) mt
cf2py intent(in) w
cf2py intent(in) wbb
cf2py intent(inout) ifo
cf2py intent(in) xbb
cf2py intent(in) ttat
cf2py intent(inout) qm
cf2py intent(in) wnu
cf2py intent(inout) lk
cf2py intent(in) ilike
cf2py intent(in) m
cf2py intent(in) p
cf2py intent(in) p1
cf2py intent(in) n
cf2py intent(in) k2
c ---------------------
      ifo = 0
      llike = 0.0

      k=k3-1
      
c     Initialise: qm      
      do i = 1, k+1
          do j = 1, k+1
              qm(i,j) = 0.0
          enddo
      enddo

      do t = 1, n
                  
c         1. Compute: Nu(t)= [0,Y(t)] - X(t)Bb - Z(t)A(t)
c         1a. Initialise nu:          
          do j = 1, k
              do i = 1, p
                  nu(i,j,t) = 0.0
              enddo
          enddo          

c         1b. Initialise last column: nu(:,k+1,t) = y(:,t)
          call dcopy(p, y(:,t), 1, nu(:,k+1,t), 1)          

c         1c. Compute: nu(t) = nu(t) - z * at
          alpha = -1.0
          beta = 1.0   
          call dgemm('n','n',p,k+1,m,alpha,z,p,at,m,beta,nu(:,:,t),p)
                              
c         1d. Compute: nu = nu - xbb
          if(k1.ne.0) then
              do j = 1, k+1
                  call daxpy(p,alpha,xbb(:,j,t),1,nu(:,j,t),1)
              enddo
          endif
!          print *, "nu(t) =", nu(:,:,t)
c         -------------------------------------------------
c         2. Compute: m(t) = P(t)*Z(t)'
          alpha = 1.0
          beta = 0.0
          call dgemm('n','t',m,p,m,alpha,pt,m,z,p,beta,mt,m)
!          print *, "m(t) =", mt
c         -------------------------------------------------
c         3. Compute: F(t) = Z(t)*m(t) + H(t)          
c         3a. Initialise: f = h
          if (p1.eq.p) then 
              do i = 1, p
                  call dcopy(p, h(:,i), 1, f(:,i), 1)
              enddo                
c             3b. Compute: f = f + z*mt
              beta = 1.0
              call dgemm('n','n',p,p,m,alpha,z,p,mt,m,beta,f,p)
          else
              call dgemm('n','n',p,p,m,alpha,z,p,mt,m,beta,f,p)
              do i=1,p
                  f(i,i)=f(i,i)+h(i,1)
              enddo
          endif
              
!          print *, "F(t) =", f
c         -------------------------------------------------
c         4. Compute: F(t)*S(t) = Z(t); solve for S(t) = inv(F(t))*Z(t)          
c         4a. Initialise: s(t) = z(t)
          do i = 1, m 
              call dcopy( p, z(:,i), 1, s(:,i,t), 1)
          enddo
c         4b. Solve system of equations          
          call dposv('u', p, m, f, p, s(:,:,t), p, info)
          if (info.ne.0) then
              ifo = 1
          endif
!          print *, "S(t) = ", s(:,:,t)

c         ------------------------------------------------- 
          if (ilike.eq.0) then
              do i = 1, p
                llike = llike - log(f(i,i))
              enddo
          endif


c         -------------------------------------------------
c         5. Compute: Qm(t) = Qm(t) + Nu(t)'*inv(F(t))*Nu(t)          
c         5a. Initialise: wnu = nu
          do j = 1, k+1
              call dcopy(p, nu(:,j,t), 1, wnu(:,j), 1)
          enddo
                        
c         5b. Compute: wnu = inv[F].Nu;  i.e. Solve F.wnu = Nu          
          call dtrsm('l','u','n','n',p,k+1,alpha,f,p,wnu,p)
!          print *, "wnu =", wnu 
          
c         5c. Compute: qm = qm + nu' * wnu          
          beta = 1.0
          call dgemm('t','n', k+1, k+1, p, alpha, nu(:,:,t), p, wnu, p,
     + beta, qm, k+1)
!          print *, "Q(t) =", qm
c         -------------------------------------------------
c         6. Compute: W(t) = T(t)*P(t)
          beta = 0.0
          call dgemm('n','n',m,m,m,alpha,tt,m,pt,m,beta,w,m)
!          print *, "W(t) =", w
c         -------------------------------------------------
c         7. Compute: K(t) = W(t)*S(t)'
          call dgemm('n','t',m,p,m,alpha,w,m,s(:,:,t),p,beta,ks(:,:,t),
     + m)
!          print *, "K(t) =", ks(:,:,t)
c         -------------------------------------------------     
c         8. Compute: L(t) = T(t) - K(t)*Z(t)
c         8a. Initialise: ls = tt
          do i = 1, m
              call dcopy(m, tt(:,i), 1, ls(:,i,t), 1)
          enddo                 
          
c         8b. Compute: ls = ls - ks * z          
          alpha = - 1.0
          beta = 1.0
          call dgemm('n','n',m,m,p,alpha,ks(:,:,t),m,z,p,beta,
     + ls(:,:,t), m)
!          print *, "L(t) =", ls(:,:,t)     
c         -------------------------------------------------                                          
c         9. Compute: a(t+1) = wbb(t) + T(t)*a(t) + K(t)*nu(t)
c         9a. Compute: ttat = tt * at
          alpha = 1.0
          beta = 0.0
          call dgemm('n','n', m,k+1,m,alpha,tt,m,at,m,beta,ttat,m)
c         9b. Initialise: at = ttat          
          do j = 1, k+1
              call dcopy(m,ttat(:,j),1,at(:,j),1)
          enddo
c         9c. Compute: at = at + ks * nu    
          beta = 1.0      
          call dgemm('n','n', m,k+1,p,alpha, ks(:,:,t),m, nu(:,:,t),
     + p, beta, at, m)
     
c         Compute: at = at + wbb  
          if (k2.ne.0) then
              do j = 1, k+1
                  call daxpy(m, beta, wbb(:,j,t), 1, at(:,j), 1)
              enddo
          endif
!          print *, "a(t) =", at
c         -------------------------------------------------
c         10. Compute: P(t+1) = W(t)*L(t)' + Q(t)
c         10a. Initialise: pt = qt
          do i = 1, m
              call dcopy(m, qt(:,i) , 1, pt(:,i), 1)
          enddo
          
c         10b. Compute: pt = pt + w*ls          
          beta = 1.0
          call dgemm('n','t',m,m,m,alpha,w,m,ls(:,:,t),m,beta,pt,m)
!          print *, "P(t) =", pt    
!          print *, " "
      enddo
      lk(1)=llike
      end

c ---------------------------------------------------------------------

c     subroutine for filtering with the standard non time varying state SSM with
c     state regressors

      subroutine ntsrfilter(y,z,h,tt,qt,nu,k,f,s,a,at,pt,ps,mt,w,ls,
     + lk,ilike,ifo,wb,wl,m,p,p1,n)
      integer m,p,n,t,i,ifo, info,chk,ilike,p1
      real*8 y(p,n),z(p,m),h(p,p1),tt(m,m),qt(m,m),lk(*)
      real*8 nu(p,n),k(m,p,n),s(p,m,n),ls(m,m,n),a(m,n)
      real*8 ps(m,m,n),mt(m,p),at(m),pt(m,m),f(p,p),w(m,m)
      real*8 alpha, beta,tol,logdet,llike,ddot,wb(m,n)
      real*8 wl(p)
c -----------------
cf2py intent(in) y
cf2py intent(in) z
cf2py intent(in) h
cf2py intent(in) tt
cf2py intent(in) qt
cf2py intent(inout) nu
cf2py intent(inout) k
cf2py intent(in) f
cf2py intent(inout) s
cf2py intent(inout) a
cf2py intent(in) at
cf2py intent(in) pt
cf2py intent(inout) ps
cf2py intent(in) mt
cf2py intent(in) w
cf2py intent(inplace) lk
cf2py intent(in) ilike
cf2py intent(inplace) ifo
cf2py intent(inout) wl
cf2py intent(in) wb
cf2py intent(in) m
cf2py intent(in) p
cf2py intent(in) p1
cf2py intent(in) n
c --------------------
      ifo=0
      tol=1E-10
      chk=10
      llike=0.0

      do t=1,n
          call dcopy(m,at,1,a(:,t),1)
          do i=1,m
              call dcopy(m,pt(:,i),1,ps(:,i,t),1)
          enddo

c         Compute: Nu(t)= Y(t) - Z(t)*a(t)     
          call dcopy(p,y(:,t),1,nu(:,t),1)
          alpha=-1.0
          beta=1.0
          call dgemv('n',p,m,alpha,z,p,at,1,beta,nu(:,t),1)
          alpha=1.0
          beta=0.0

c         Compute: m(t) = P(t)*Z(t)'          
          call dgemm('n','t',m,p,m,alpha,pt,m,z,p,beta,mt,m)


c         Compute: F(t) = Z(t)*m(t)+H(t)          
          if (p1.eq.p) then
              do i=1,p
                  call dcopy(p,h(:,i),1,f(:,i),1)
              enddo
              beta=1.0
              call dgemm('n','n',p,p,m,alpha,z,p,mt,m,beta,f,p)
          else
              call dgemm('n','n',p,p,m,alpha,z,p,mt,m,beta,f,p)
              do i=1,p
                  f(i,i) = f(i,i) + h(i,1)
              enddo
          endif
              

c         Compute: F(t)*S(t) = Z(t); solve for S(t)=inv(F(t))*Z(t)          
          do i=1,m
              call dcopy(p,z(:,i),1,s(:,i,t),1)
          enddo
          call dposv('u',p,m,f,p,s(:,:,t),p,info)
          if (info.ne.0) then
              ifo=1
          endif
          beta=0.0
          if (ilike.eq.0) then
              logdet=0.0
              do i=1,p
                  logdet=logdet+log(f(i,i))
              enddo
              logdet=logdet*2.0
              
              call dcopy(p,nu(:,t),1,wl,1)
              call dtrsm('l','u','t','n',p,1,alpha,f,p,wl,p)
              call dtrsm('l','u','n','n',p,1,alpha,f,p,wl,p)
              llike=llike-0.5*(logdet+ddot(p,wl,1,nu(:,t),1))
          endif
      
c         Compute: W(t) = T(t)*P(t)
          call dgemm('n','n',m,m,m,alpha,tt,m,pt,m,beta,w,m)

c         Compute: K(t) = W(t)*S(t)'
          call dgemm('n','t',m,p,m,alpha,w,m,s(:,:,t),p,beta,
     + k(:,:,t),m)

c         Compute: L(t)=T(t)-K(t)*Z(t)
          do i=1,m
              call dcopy(m,tt(:,i),1,ls(:,i,t),1)
          enddo
          alpha=-1.0
          beta=1.0
          call dgemm('n','n',m,m,p,alpha,k(:,:,t),m,z,p,beta,
     + ls(:,:,t),m)

          alpha=1.0
          beta=0.0

c         Compute: a(t+1)=wb(t)+T(t)*a(t)+K(t)*nu(t)
          call dgemv('n',m,m,alpha,tt,m,a(:,t),1,beta,at,1)
          beta=1.0
          call dgemv('n',m,p,alpha,k(:,:,t),m,nu(:,t),1,beta,at,1)
          beta=0.0
              
          call daxpy(m,alpha,wb(:,t),1,at,1)

c         Compute: P(t+1)=W(t)*L(t)'+Q(t)
          do i=1,m
              call dcopy(m,qt(:,i),1,pt(:,i),1)
          enddo
          beta=1.0
          call dgemm('n','t',m,m,m,alpha,w,m,ls(:,:,t),m,beta,pt,m)
      enddo
      lk(1)=llike
      end

c ---------------------------------------------------------------------

c     subroutine calculates the Frobenius norm for the difference of two matrices
      real*8 function fnorm(a,b,m,n)
      implicit none
      integer m,n,i,j
      real*8 a(m,n),b(m,n), sumd

      sumd=0.0
      do j=1,n
          do i=1,m
              sumd=sumd+(a(i,j)-b(i,j))**2
          enddo
      enddo
      fnorm=sqrt(sumd)
      return
      end


c ---------------------------------------------------------------------
c     subroutine used to update XBb
      subroutine update_xbb(xbb,x,bb,p,km,n,k,kp1)
      implicit none
      integer km,n,k,kp1,t,ks,km1,p
      real*8 x(p,km,n),bb(k,kp1),xbb(p,kp1,n)
      real*8 alpha,beta

      ks=k-km+1
      km1=km+1
      alpha=1.0
      beta=0.0

      do t=1,n
          call dgemm('n','n',p,km1,km,alpha,x(:,:,t),p,bb(ks:k,ks:kp1),
     + km,beta,xbb(:,ks:kp1,t),p)
      enddo
      
      end subroutine update_xbb
            
c ---------------------------------------------------------------------
c     subroutine to update WBb
            subroutine update_wbb(wbb,w,bb,m,ks,n,k,kp1)
            implicit none
            integer m,ks,n,k,kp1,t
            real*8 wbb(m,kp1,n),w(m,ks,n),bb(k,kp1)
            real*8 alpha,beta

            alpha=1.0
            beta=0.0

            do t=1,n
                call dgemm('n','n',m,ks,ks,alpha,w(:,:,t),m,
     + bb(1:ks,1:ks),ks,beta,wbb(:,1:ks,t),m)
                call dgemv('n',m,ks,alpha,w(:,:,t),m,bb(1:ks,kp1),1,
     + beta,wbb(:,kp1,t),1)
                
            enddo
            end subroutine update_wbb
            

c ---------------------------------------------------------------------

c     subroutine used to update xbeta and wbeta
      subroutine update_xwbeta(x,b,xb,p,k,n)
      implicit none
      integer p,k,n,t
      real*8 x(p,k,n),b(k),xb(p,n)
      real*8 alpha,beta
c -------------------
cf2py intent(in) x
cf2py intent(in) b
cf2py intent(inout) xb
cf2py intent(in) p
cf2py intent(in) k
cf2py intent(in) n
c -------------------
      alpha=1.0
      beta=0.0
c$omp parallel shared(x,b,xb)
c$omp do schedule(static)
      do t=1,n
          call dgemv('n',p,k,alpha,x(:,:,t),p,b,1,beta,xb(:,t),1)
      enddo
c$omp end do
c$omp end parallel
      end

c ---------------------------------------------------------------------

c     subroutine calulates residuals in state equation with regressors
      subroutine rstate_res(st,tt,res,wb,n,m, n_t)
      implicit none
      integer n,m,t, t_t, n_t, timet
      real*8 st(m,n),tt(m,m,n_t),res(m,n-1),wb(m,n)
      real*8 alpha, beta
c ----------------------
cf2py intent(in) st
cf2py intent(in) tt
cf2py intent(in) wb
cf2py intent(inout) res
cf2py intent(in) n
cf2py intent(in) m
c ------------------
      alpha = -1.0
      beta = 1.0

c$omp parallel default(shared) private(t, t_t)
c$omp do schedule(static)
      do t = 1, n-1
          t_t = timet(n_t, t)

c         Initialise: res(t) = st(t+1)          
          call dcopy(m, st(:,t+1), 1 ,res(:,t),1)

c         Compute: res(t) = res(t) - tt * st(t)          
          call dgemv('n',m,m,alpha,tt(:,:,t_t),m,st(:,t),1,beta,
     + res(:,t),1)
     
c         Compute: res(t) = res(t) - wb(t)     
          call daxpy(m, alpha, wb(:,t), 1, res(:,t), 1)
     
      enddo
c$omp end do
c$omp end parallel

      end

c ---------------------------------------------------------------------

c     non-time varying verions of state_res with regressors
      subroutine rntstate_res(st,tt,res,wb,n,m)
      implicit none
      integer n,m,t
      real*8 st(m,n),tt(m,m),res(m,n-1),wb(m,n)
      real*8 alpha, beta
c --------------------
cf2py intent(in) st
cf2py intent(in) tt
cf2py intent(in) wb
cf2py intent(inout) res
cf2py intent(in) n
cf2py intent(in) m
c ------------------

      alpha = -1.0
      beta = 1.0
      
c$omp parallel default(shared) private(t) 
c$omp do schedule(static)
      do t = 1, n-1

c         Initialise: res(t) = st(t+1)                
          call dcopy(m,st(:,t+1),1,res(:,t),1)
          
c         Compute: res(t) = res(t) - tt * st(t)                    
          call dgemv('n',m,m,alpha,tt,m,st(:,t),1,beta,
     + res(:,t),1)
     
c         Compute: res(t) = res(t) - wb(t)          
          call daxpy(m,alpha,wb(:,t),1,res(:,t),1)
      enddo
c$omp end do
c$omp end parallel

      end

c ---------------------------------------------------------------------

c **/** NEW OPENMP ADDED - UNTESTED **/**

c      subroutine to calculate the state vector given the initial state
c      and the state disturbances with regressors
       subroutine rgenstate(eta,tt,gt,st,wb,m,r,n, n_t, n_g)
       implicit none
       integer n,m,r,t, n_t, n_g, t_t, t_g, timet
       real*8 eta(r,n),tt(m,m,n_t),gt(m,r,n_g),st(m,n)
       real*8 wb(m,n)
       real*8 alpha,beta
c --------------------
cf2py intent(in) eta
cf2py intent(in) tt
cf2py intent(in) gt
cf2py intent(in) wb
cf2py intent(inout) st
cf2py intent(in) m
cf2py intent(in) r
c -------------------
      alpha = 1.0      
       
c$omp parallel default(shared) private(t, t_g, beta)
c$omp do schedule(static)      
      do t = 1, n-1     
        
          t_g = timet(n_g, t)    
                
c         Compute: st(t+1) = gt(t) * eta(:,t) 
          beta = 0.0              
          call dgemv('n',m,r,alpha,gt(:,:,t_g),m,eta(:,t),1,beta,
     + st(:,t+1),1)
          
c         Compute: st(t+1) = st(t+1) + alpha * wb(t) 
          beta = 1.0    
          call daxpy(m,alpha, wb(:,t), 1, st(:,t+1), 1)
      enddo
c$omp end do
c$omp end parallel

      beta = 1.0
      
      do t = 1, n-1           
          t_t = timet(n_t, t)                         

c         Compute: st(t+1) = tt(t) * st(t)
          call dgemv('n',m,m,alpha,tt(:,:,t_t),m,st(:,t),1,beta,
     + st(:,t+1), 1)
     
      enddo
           
      end
         
c ---------------------------------------------------------------------
      
c **/** NEW OPENMP ADDED - UNTESTED **/**      
         
c      subroutine to calculate the state vector given the initial state
c      and the state disturbances and non time varying system matricies
       subroutine ntrgenstate(eta,tt,gt,st,wb,m,r,n)
       implicit none
       integer n,m,r,t
       real*8 eta(r,n),tt(m,m),gt(m,r),st(m,n),wb(m,n)
       real*8 alpha,beta
c -----------------------
cf2py intent(in) eta
cf2py intent(in) tt
cf2py intent(in) gt
cf2py intent(inout) st
cf2py intent(in) wb
cf2py intent(in) m
cf2py intent(in) r
c --------------------

      alpha = 1.0
     
c$omp parallel default(shared) private(t, beta)      
c$omp do schedule(static)
      do t = 1, n-1
            
c         Compute: st(t+1) = gt * eta(:,t)                    
          beta = 0.0
          call dgemv('n',m,r,alpha,gt,m,eta(:,t),1,beta,st(:,t+1),
     + 1)
c         Compute: st(t+1) = st(t+1) + wb(t)     
          beta = 1.0
          call daxpy(m,alpha,wb(:,t),1,st(:,t+1),1)
      enddo
c$omp end do
c$omp end parallel

      beta = 1.0   
      do t = 1, n-1

c         Compute: st(t+1) = st(t+1) + tt * st(t)                      
          call dgemv('n',m,m,alpha,tt,m,st(:,t),1,beta,st(:,t+1), 1)
      enddo
      
      end
c ----------------------------------------------------------------------

c **/** NEW OPENMP ADDED - UNTESTED **/**

c     Procedure called from within augmented smoother in ssm.py
      subroutine update_nustore(a, b, c, p, k, n)
      implicit none
      integer t, n, k, p
      real*8 a(p,n), b(p,k,n), c(k), alpha, beta
c     Note: a == nustore
c     Note: b = Nustore
c     Note: c = hstack([delta, 1.0]) 
c -----------------------
cf2py intent(inout) a
cf2py intent(in) b
cf2py intent(in) c
cf2py intent(in) p
cf2py intent(in) k
cf2py intent(in) n
c ----------------------
      alpha = 1.0
      beta = 0.0  
      
c$omp parallel default(shared) private(t)
c$omp do schedule(static)
      do t = 1, n           
c         Compute: a(:,t) = b(:,:,t) * c
          call dgemv('n', p, k, alpha, b(:,:,t), p, c, 1, beta, 
     + a(:,t), 1)              
      enddo
c$omp end do
c$omp end parallel
      
      end     
c ----------------------------------------------------------------------
        
      subroutine calcxbeta(x,b,xb,n,m,k)
      implicit none
      integer n,m,k,t
      real*8 x(m,k,n),xb(m,n),b(k)
      real*8 alpha, beta

cf2py intent(in) x
cf2py intent(in) b
cf2py intent(inout) xb
cf2py intent(in) n
cf2py intent(in) m
cf2py intent(in) k

      alpha = 1.0
      beta = 0.0
c$omp parallel default(shared) private(t)
c$omp do schedule(static)
      do t=1,n
          call dgemv('n',m,k,alpha,x(:,:,t),m,b,1,beta,xb(:,t),1)
      enddo
c$omp end do
c$omp end parallel
      end subroutine calcxbeta
      
