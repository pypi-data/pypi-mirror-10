c FORTRAN77 source code for the Python library PySSM
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



c ----------------------------------------------------------------------
c     fortran code for univariate filtering algorithms
c ----------------------------------------------------------------------
      
       subroutine unifilter(y, nf, k, at, pt, a, pm, z, h, mt, tt, q,
     + pttt, lk, ptt, ilike, p, m, n, nz, nh, nt, nq)     
     
      implicit none
      integer p,m,n,ptt,i,t,j,ilike
      integer tz,th,t_t,tq,timet
      integer nz, nh, nt, nq
      real*8 y(p,n), nf(p,n,2), k(m,p,n), at(m,n), pt(m,m,n)
      real*8 q(m,m,nq), mt(m), tt(m,m,nt), h(p,1,nh), pttt(m,m)
      real*8 a(m), pm(m,m), lk(*),llike, z(p,m,nz)
      real*8 ddot, alpha, beta,as


c     y - (p*n) is a matrix containing the dependent variable
c     nf - (p*n*2) nf(:,1) is nustore, nf(:,2) is fstore
c     ka - (m,p+1,n,2) ka(:,:,1)= kstore, ka(:,:,2) is astore
c     pt - (m,m,p+1,n) 
c     z - (m,p,n) is the system matrix Zt
c     h - (p*n) is the system matrix Ht. Note that Ht is diagonal
c     q - (m*m*n) is the system matrix r, q=GQG'
c     w - (m,m) is a work array.
c ----------------------
cf2py intent(in) y
cf2py intent(inout) nf
cf2py intent(inout) k
cf2py intent(inout) at
cf2py intent(inout) pt
cf2py intent(in) a
cf2py intent(in) pm
cf2py intent(in) z
cf2py intent(in) h
cf2py intent(in) mt
cf2py intent(in) tt
cf2py intent(in) pttt
cf2py intent(in) ptt
cf2py intent(inout) lk
cf2py intent(in) q
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) nz
cf2py intent(in) nh
cf2py intent(in) nt
cf2py intent(in) nq
c ---------------------
      llike = 0.0
              
      do t = 1, n
      
          tz = timet(nz,t)
          th = timet(nh,t)
          t_t = timet(nt,t)          
          tq = timet(nq,t)

          call dcopy(m,a,1,at(:,t),1)
          do j = 1, m
              call dcopy(m, pm(:,j),1, pt(:,j,t),1) 
          enddo
          
          do i = 1, p

              alpha = 1.0
              beta = 0.0
              if (isnan(y(i,t)).eqv..FALSE.) then
                  nf(i,t,1) = y(i,t) - ddot(m,z(i,:,tz),1,a,1)
                  
                  call dgemv('n',m,m,alpha,pm,m,z(i,:,tz),1,beta,mt,
     + 1)
                  
                  nf(i,t,2) = ddot(m,z(i,:,tz),1,mt,1) + h(i,1,th)
                  do j = 1, m
                      k(j,i,t) = mt(j) / nf(i,t,2)
                      as = a(j) + k(j,i,t)*nf(i,t,1)
                      a(j) = as
                  enddo
                  alpha = -1.0
                  call dger(m,m,alpha,k(:,i,t),1, mt,1, pm,m)
                  if (ilike.eq.0) then
                      llike = llike - 0.5*(log(nf(i,t,2))+nf(i,t,1)**2 /
     + nf(i,t,2))
                  endif
              endif
          enddo
          alpha = 1.0
          if (ptt.eq.0) then
              call dgemv('n',m,m,alpha,tt(:,:,t_t),m,a,1,beta,
     + pttt(:,1),1)
              call dcopy(m,pttt(:,1),1,a,1)
          endif
          if (ptt.eq.0) then
              alpha = 1.0
              beta = 0.0
              call dgemm('n','t',m,m,m,alpha,pm,m,tt(:,:,t_t),m,beta,
     +  pttt,m)
              do i = 1, m
                  call dcopy(m, q(:,i,tq),1, pm(:,i),1)
              enddo
              beta = 1.0
              call dgemm('n','n',m,m,m,alpha, tt(:,:,t_t),m,pttt,m,beta,
     + pm,m) 
          else
              do j = 1, m
                  call daxpy(m,alpha, q(:,j,tq),1, pm(:,j),1)
              enddo
          endif
      enddo
      lk(1)=llike
      end
      
c ----------------------------------------------------------------------

c     non - timvaring verion of the univariate filtering algorithm      
      subroutine ntunifilter(y,nf,k,at,pt,a,pm,z,h,mt,tt,q,pttt,lt,
     + lk,ilike,p,m,n)
      implicit none
      integer p,m,n,i,t,j,chk,indr,lt,ilike
      real*8 y(p,n), nf(p,n,2), k(m,p,n), at(m,n), pt(m,m,n)
      real*8 q(m,m), mt(m,p), tt(m,m), h(p), pttt(m,m), z(p,m)
      real*8 a(m), pm(m,m),lk(*),llike
      real*8 ddot, alpha, beta,as, fnormv,tol


c     y - (p*n) is a matrix containing the dependent variable
c     nf - (p*n*2) nf(:,1) is nustore, nf(:,2) is fstore
c     ka - (m,p+1,n,2) ka(:,:,1)= kstore, ka(:,:,2) is astore
c     pt - (m,m,p+1,n) 
c     z - (m,p,n) is the system matrix Zt
c     h - (p*n) is the system matrix Ht. Note that Ht is diagonal
c     q - (m*m*n) is the system matrix r, q=GQG'
c     w - (m,m) is a work array.
c -----------------------
cf2py intent(in) y
cf2py intent(inout) nf
cf2py intent(inout) k
cf2py intent(inout) at
cf2py intent(inout) pt
cf2py intent(in) a
cf2py intent(in) pm
cf2py intent(in) z
cf2py intent(in) h
cf2py intent(in) mt
cf2py intent(in) tt
cf2py intent(in) pttt
cf2py intent(inout) lt
cf2py intent(inout) lk
cf2py intent(in) q
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
c -----------------------
      tol=1E-10
      chk=10
      indr=0
      lt=n+1      
      llike=0.0
      do t=1,n
          call dcopy(m,a,1,at(:,t),1)
          do j=1,m
              call dcopy(m,pm(:,j),1,pt(:,j,t),1) 
          enddo
          if (indr.ne.1) then

              do i=1,p
                  alpha=1.0
                  beta=0.0

c                 Compute: nu(t,i) = y(t,i) - z(t,i)'a(t,i)
                  nf(i,t,1)=y(i,t)-ddot(m,z(i,:),1,a,1)

c                 Compute: m(t,i) = P(t,i) * z(t,i)
                  call dgemv('n',m,m,alpha,pm,m,z(i,:),1,beta,mt(:,i),1)

c                 Compute: f(t,i) = z(t,i)'m(t,i) + 1
                  nf(i,t,2)=ddot(m,z(i,:),1,mt(:,i),1)+h(i)
                  
                  do j = 1, m

c                     Compute: k(t,i) = m(t,i) / f(t,i)
                      k(j,i,t)=mt(j,i)/nf(i,t,2)

c                     Compute: a(t,i+1) = a(t,i) + k(t,i) * nu(t,i)
                      as=a(j)+k(j,i,t)*nf(i,t,1)
                      a(j)=as
                  enddo
                  
                  alpha=-1.0

c                 Compute: P(t,i+1) = P(t,i) - k(t,i) * m(t,i)'
                  call dger(m,m,alpha,k(:,i,t),1,mt(:,i),1,pm,m)
                  if (ilike.eq.0) then
                      llike=llike-0.5*(log(nf(i,t,2))+nf(i,t,1)*
     + nf(i,t,1)/nf(i,t,2))
                  endif
              enddo
              alpha=1.0
              
c             Compute: a(t+1,i) = T(t) * a(t,p+1)
              call dgemv('n',m,m,alpha,tt,m,a,1,beta,pttt(:,1),1)
              call dcopy(m,pttt(:,1),1,a,1)
              alpha=1.0
              beta=0.0
              
c             Compute: P(t+1,i) = T(t) * P(t,p+1)T(t)' + G(t)*inv(Q)*G(t)'
              call dgemm('n','t',m,m,m,alpha,pm,m,tt,m,beta, pttt,m)
              do i=1,m
                  call dcopy(m,q(:,i),1,pm(:,i),1)
              enddo
              beta=1.0
              call dgemm('n','n',m,m,m,alpha,tt,m,pttt,m,beta,pm,m) 

c             Monitor convergence to steady state
              if (mod(t,chk).eq.0) then
                  if (fnormv(nf(:,t,2),nf(:,t-chk,2),p).lt.tol) then
                      indr=1
                      lt=t
                  endif
              endif
          else
              do i=1,p
                  alpha=1.0
                  beta=0.0
                  nf(i,t,1)=y(i,t)-ddot(m,z(i,:),1,a,1)
                  do j=1,m
                      as=a(j)+k(j,i,lt)*nf(i,t,1)
                      a(j)=as
                  enddo
                  alpha=-1.0
                  call dger(m,m,alpha,k(:,i,lt),1,mt(:,i),1,pm,m)
                  if (ilike.eq.0) then
                      llike=llike-0.5*(log(nf(i,lt,2))+nf(i,t,1)**2/

     + nf(i,lt,2))
                  endif
              enddo
              alpha=1.0
              call dgemv('n',m,m,alpha,tt,m,a,1,beta,pttt(:,1),1)
              call dcopy(m,pttt(:,1),1,a,1)
              alpha=1.0
              beta=0.0
              call dgemm('n','t',m,m,m,alpha,pm,m,tt,m,beta, pttt,m)
              do i=1,m
                  call dcopy(m,q(:,i),1,pm(:,i),1)
              enddo
              beta=1.0
              call dgemm('n','n',m,m,m,alpha,tt,m,pttt,m,beta,pm,m) 
          endif
      enddo
      lk(1)=llike
      end

c ----------------------------------------------------------------------

c     smoothing routine for univariate filter
      subroutine unismoother2(ah,k,a,pt,r,tt,z,ltr,nf,ptt,y,p,m,n,
     + nz,nt)
      implicit none
      integer ptt,p,m,n,i,t,j
      integer nz,nt, t_z, timet
      real*8 ah(m,n), k(m,p,n), a(m,n), pt(m,m,n), r(m)
      real*8 tt(m,m,nt), z(p,m,nz), nf(p,n,2), ltr(m) 
      real*8 alpha, beta, dzr, ddot, y(p,n)
c -----------------------
cf2py intent(inout) ah
cf2py intent(in) k
cf2py intent(inout) a
cf2py intent(in) pt
cf2py intent(in) r
cf2py intent(in) tt
cf2py intent(in) z
cf2py intent(in) lt
cf2py intent(in) ltr
cf2py intent(in) nf
cf2py intent(in) ptt
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
c -----------------------
      do i = 1, m
          r(i)=0.0
      enddo
      
c     ah - (m,n) matrix ahat

      do t = n, 1, -1
          t_z = timet(nz,t)

          do i = p, 1, -1
              if (isnan(y(i,t)).eqv..FALSE.) then
                  dzr = ddot(m,k(:,i,t),1,r,1)
                  do j = 1, m
                      ltr(j) = r(j)- z(i,j,t_z) * dzr
                      r(j) = z(i,j,t_z) * nf(i,t,1) / nf(i,t,2) + ltr(j)
                  enddo
              endif
          enddo
          call dcopy(m,a(:,t),1,ah(:,t),1)
          alpha=1.0
          beta=1.0
          call dgemv('n',m,m,alpha,pt(:,:,t),m,r,1,beta,ah(:,t),1)
          beta=0.0
          if (ptt.eq.0) then
              if (t.gt.1) then
                  
                  if (nt.gt.1) then
                      call dgemv('t',m,m,alpha,tt(:,:,t-1),m,r,1,beta,
     + ltr,1)
                  else
                      call dgemv('t',m,m,alpha,tt(:,:,1),m,r,1,beta,
     + ltr,1)
                  endif
                  call dcopy(m,ltr,1,r,1)
              endif
          endif
      enddo
      end


c ----------------------------------------------------------------------
      
      subroutine ntunismoother2(ah,k,a,pt,r,tt,z,ltr,nf,it,p,m,n)
      implicit none
      integer p,m,n,i,t,j,it,lt
      real*8 ah(m,n),k(m,p,n),a(m,n), pt(m,m,n), r(m)
      real*8 tt(m,m),z(p,m),nf(p,n,2), ltr(m) 
      real*8 alpha, beta,dzr,ddot
c -----------------------
cf2py intent(inout) ah
cf2py intent(in) k
cf2py intent(inout) a
cf2py intent(in) pt
cf2py intent(in) r
cf2py intent(in) tt
cf2py intent(in) z
cf2py intent(in) lt
cf2py intent(in) ltr
cf2py intent(in) nf
cf2py intent(in) it
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
c -----------------------
      do i = 1, m
          r(i) = 0.0
      enddo
      
      alpha = 1.0
      
c     ah - (m,n) matrix ahat
      do t = n, 1, -1
          if (t.lt.it) then
              lt=t
          else
              lt=it
          endif

          do i = p, 1, -1

c             Compute:   dzr = k dot r        
              dzr = ddot(m,k(:,i,lt),1,r,1)
              
              do j=1,m
                  ltr(j) = r(j) - z(i,j)*dzr
                  r(j) = z(i,j) * nf(i,t,1) / nf(i,lt,2) + ltr(j)
              enddo
          enddo
          
c         Initialise: ah(t) = a(t)          
          call dcopy(m,a(:,t),1,ah(:,t),1)
                              
c         Compute: ah(t) = ah(t) + pt(t) * r          
          beta = 1.0
          call dgemv('n',m,m,alpha,pt(:,:,t),m,r,1,beta,ah(:,t),1)
          
          beta = 0.0
          if (t.gt.1) then
c             Compute: ltr = tt * r         
              call dgemv('t',m,m,alpha,tt,m,r,1,beta,ltr,1)
c             Initialise: r = ltr              
              call dcopy(m,ltr,1,r,1)
          endif
      enddo
      end

c ----------------------------------------------------------------------

c     smoothing routine for univariate filter
      subroutine unismoother(ah,k,a,pt,r,tt,z,lt,ltr,nf,p,m,n,
     + nz,nt)
      implicit none
      integer p,m,n,i,t,j,nz,nt,tz,t_t,timet
      real*8 ah(m,n),k(m,p,n),a(m,n), pt(m,m,n), r(m)
      real*8 tt(m,m,n),z(p,m,n), lt(m,m), nf(p,n,2), ltr(m) 
      real*8 alpha, beta
c -----------------------
cf2py intent(inout) ah
cf2py intent(in) k
cf2py intent(inout) a
cf2py intent(in) pt
cf2py intent(in) r
cf2py intent(in) tt
cf2py intent(in) z
cf2py intent(in) lt
cf2py intent(in) ltr
cf2py intent(in) nf
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
c -------------------
      do i=1,m
          r(i)=0.0
      enddo
c     ah - (m,n) matrix ahat
      do t=n,1,-1
          tz=timet(nz,t)
          t_t=timet(nt,t)

          do i=p,1,-1
              alpha=-1.0
              call eye(lt,m)
              call dger(m,m,alpha,k(:,i,t),1,z(i,:,tz),1,lt,m)
              alpha=1.0
              beta=0.0
              call dgemv('t',m,m,alpha,lt,m,r,1,beta,ltr,1)
              do j=1,m
                  r(j)=z(i,j,t)*nf(i,t,1)/nf(i,t,2)+ltr(j)
              enddo
          enddo
          call dcopy(m,a(:,t),1,ah(:,t),1)
          alpha=1.0
          beta=1.0
          call dgemv('n',m,m,alpha,pt(:,:,t),m,r,1,beta,ah(:,t),1)
          beta=0.0
          if (t.gt.1) then
              if (nt.gt.1) then
                  call dgemv('t',m,m,alpha,tt(:,:,t-1),m,r,1,beta,
     + ltr,1)
              else
                  call dgemv('t',m,m,alpha,tt(:,:,1),m,r,1,beta,
     + ltr,1)
              endif
              call dcopy(m,ltr,1,r,1)

          endif
      enddo
      end

c ----------------------------------------------------------------------  
    
      subroutine ntunismoother(ah,k,a,pt,r,tt,z,lt,ltr,nf,it,p,m,n)
      implicit none
      integer p,m,n,i,t,j,it
      real*8 ah(m,n), k(m,p,n), a(m,n), pt(m,m,n), r(m)
      real*8 tt(m,m),z(p,m), lt(m,m,p), nf(p,n,2), ltr(m) 
      real*8 alpha, beta
c ----------------------
cf2py intent(inout) ah
cf2py intent(in) k
cf2py intent(inout) a
cf2py intent(in) pt
cf2py intent(in) r
cf2py intent(in) tt
cf2py intent(in) z
cf2py intent(in) lt
cf2py intent(in) ltr
cf2py intent(in) nf
cf2py intent(in) it
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
c ------------------
      do i=1,m
          r(i)=0.0
      enddo
c     ah - (m,n) matrix ahat
      do t=n,1,-1
          if (t.lt.it) then
              do i=p,1,-1
                  alpha=-1.0
                  call eye(lt(:,:,i),m)
                  call dger(m,m,alpha,k(:,i,t),1,z(i,:),1,lt(:,:,i),m)
                  alpha=1.0
                  beta=0.0
                  call dgemv('t',m,m,alpha,lt(:,:,i),m,r,1,beta,ltr,1)
                  do j=1,m
                      r(j)=z(i,j)*nf(i,t,1)/nf(i,t,2)+ltr(j)
                  enddo
              enddo
              call dcopy(m,a(:,t),1,ah(:,t),1)
              alpha=1.0
              beta=1.0
              call dgemv('n',m,m,alpha,pt(:,:,t),m,r,1,beta,ah(:,t),1)
              beta=0.0
              if (t.gt.1) then
                  call dgemv('t',m,m,alpha,tt,m,r,1,beta,ltr,1)
                  call dcopy(m,ltr,1,r,1)
              endif
          else
              do i=p,1,-1
                  if (t.eq.n) then
                      alpha=-1.0
                      call eye(lt(:,:,i),m)
                      call dger(m,m,alpha,k(:,i,it),1,z(i,:),1,
     + lt(:,:,i),m)
                  endif
                  alpha=1.0
                  beta=0.0
                  call dgemv('t',m,m,alpha,lt(:,:,i),m,r,1,beta,ltr,1)
                  do j=1,m
                      r(j)=z(i,j)*nf(i,t,1)/nf(i,it,2)+ltr(j)
                  enddo
              enddo
              call dcopy(m,a(:,t),1,ah(:,t),1)
              alpha=1.0
              beta=1.0
              call dgemv('n',m,m,alpha,pt(:,:,t),m,r,1,beta,ah(:,t),1)
              beta=0.0
              if (t.gt.1) then
                  call dgemv('t',m,m,alpha,tt,m,r,1,beta,ltr,1)
                  call dcopy(m,ltr,1,r,1)
              endif

          endif
      enddo
      end

c ----------------------------------------------------------------------

c     subroutine calculates z * alpha  for the time varying cass
      subroutine zt_alpha(zt,st,ztst,p,m,n,nz)
      implicit none
      integer p,m,n,t,tz,nz,timet
      real*8 zt(p,m,nz),st(m,n),ztst(p,n)
      real*8 alpha, beta
c ------------------
cf2py intent(in) zt      
cf2py intent(in) st      
cf2py intent(inout) ztst     
cf2py intent(in) p      
cf2py intent(in) m      
cf2py intent(in) n      
c -----------------
      alpha = 1.0
      beta = 0.0        
      
c$omp parallel default(shared) private(t, tz)
c$omp do schedule(static)
      do t = 1, n
          tz = timet(nz,t)
          call dgemv('n',p,m,alpha,zt(:,:,tz),p,st(:,t),1,beta,
     + ztst(:,t),1)
      enddo
c$omp end do
c$omp end parallel
      end

c ----------------------------------------------------------------------

c     subroutine calulates residuals in measurement equation - time varying case
c     res = inv[rt] * [y - (zt * st) ]
      subroutine meas_res(y, zt, st, res, rt, rt_eye, rt_eps, p, m, n,
     + n_z, p1, n_r)
          
      implicit none
      integer p, m, n, t, n_z, t_z, timet, n_r, p1, t_r, info, i, rt_eye
      integer rt_eps
      real*8 y(p,n), zt(p,m,n_z), st(m,n), res(p,n), rt(p, p1, n_r)
      real*8 alpha, beta, wk(p)
c -----------------
cf2py intent(in) y
cf2py intent(in) zt
cf2py intent(in) st
cf2py intent(inout) res
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
c -------------------

      alpha = -1.0
      beta = 1.0            
            
c$omp parallel default(shared)
c$omp do schedule(static) private(t, t_z)
      do t = 1, n
          t_z = timet(n_z, t)          
          
c         1. Compute: res(t) = y(t) - z(t) * st(t)
c         1a. Initialise: res(:,t) = y(:,t)                    
          call dcopy(p, y(:,t), 1, res(:,t), 1)
          
c         1b. Compute: res(:t) = res(:,t) - zt * st(:t)  [i.e. (p,1) = (p,m)*(m) ]
          call dgemv('n', p, m, alpha, zt(:,:,t_z), p, st(:,t), 1, beta,
     + res(:,t), 1)
      enddo
c$omp end do
      if (rt_eps.eq.0) then
c     --------------------------------
c         rt is not an identity matrix
          if (rt_eye.eq.0) then
      
              if (p1.eq.1) then 
c             Case: rt is diagonal  

c$omp do schedule(static) private(t, t_r, i)     
                  do t = 1, n    
                      t_r = timet(n_r, t)
          
c                     2. Compute: res(:,t) = inv[rt] * res(:,t) where inv[rt](i) = 1 / rt(i)
                      do i = 1, p
                          res(i,t) = res(i,t) / rt(i, 1, t_r)
                      enddo
                  enddo        
c$omp end do          
c         -------------------------------      
              else
c         Case: r(t) is dense
      
c                 i.e. rt(:,:,t)  = rt(:,:,1) for all t
                  if (n_r.eq.1) then
              
c                     3. Solve: rt.x = res  [i.e. (p,p) * (p,n) = (p,n) ]
                      call dgesv(p, n, rt(:,:,1), p, wk, res, p, info)
                      if (info.gt.0) then
                          print *, "Error: Solve failed [ntmeas_res]"
                          stop
                      endif      
                  else                      
c$omp do schedule(static) private(t, info)          
                      do t = 1, n
                          call dgesv(p,1,rt(:,:,t),p, wk,res(:,t),p,
     + info)
                           if (info.gt.0) then
                              print *,"Error: Solve failed [ntmeas_res]"
                              stop
                          endif 
                      enddo                             
c$omp end do
                   endif
              endif
          endif      
      
c$omp end parallel
      endif

      end

c ----------------------------------------------------------------------

c     non time varying version of the meas_res
      subroutine ntmeas_res(y, zt, st, res, rt, rt_eye, rt_eps,p, m,
     +  n, p1)
      implicit none
      integer p, m, n, t, i, info, p1, rt_eye, rt_eps
      real*8 y(p,n), zt(p,m), st(m,n), res(p,n), rt(p, p1)
      real*8 alpha, beta, wk(p)

c -----------------
cf2py intent(in) y
cf2py intent(in) zt
cf2py intent(in) st
cf2py intent(inout) res
cf2py intent(in) rt
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
cf2py intent(in) p1
c ------------------

      alpha = -1.0
      beta = 1.0
      
c$omp parallel default(shared)
c$omp do schedule(static) private(t)      
      do t = 1, n
          
c         1. Compute: res(t) = y(t) - z(t) * st(t)
c         1a. Initialise: res(:,t) = y(:,t)          
          call dcopy(p, y(:,t), 1, res(:,t), 1)
          
c         1b. Compute: res(:t) = res(:,t) - zt * st(:t)  [i.e. (p,1) = (p,m)*(m) ]
          call dgemv('n', p, m, alpha, zt, p, st(:,t), 1, beta,
     + res(:,t), 1)
      enddo
c$omp end do
      if (rt_eps.eq.0) then
c     ------------------------------
c         rt is not an identity matrix
          if (rt_eye.eq.0) then
      
              if(p1.eq.1) then 
c             Case: rt is diagonal  

c$omp do schedule(static)  private(t, i)     
                  do t = 1, n    
c                     2. Compute: res(:,t) = inv[rt] * res(:,t) where inv[rt](i) = 1 / rt(i)
                      do i = 1, p
                          res(i,t) = res(i,t) / rt(i,1)
                      enddo
                  enddo        
c$omp end do          
c         -------------------------------      
             else
c         Case: rt is dense
                                          
c                 3. Solve: rt.x = res  [i.e. (p,p) * (p,n) = (p,n) ]
                  call dgesv(p, n, rt, p, wk, res, p, info)

                  if (info.gt.0) then
                      print *, "Error: Solve failed [ntmeas_res (2.)]"
                      stop
                  endif       
              endif    
          endif
c     -----------------------------
c$omp end parallel
      endif
      end subroutine ntmeas_res

c ----------------------------------------------------------------------

c     subroutine calulates residuals in state equation
      subroutine state_res(st,tt,res,n,m,nt)
      implicit none
      integer n,m,t,nt,t_t,timet
      real*8 st(m,n),tt(m,m,nt),res(m,n-1)
      real*8 alpha, beta
c -------------------
cf2py intent(in) st
cf2py intent(in) tt
cf2py intent(inout) res
cf2py intent(in) n
cf2py intent(in) m
c ------------------

      alpha = -1.0
      beta = 1.0
      
c$omp parallel default(shared) private(t, t_t)
c$omp do schedule(static)
      do t = 1, n-1
          t_t = timet(nt,t)
          call dcopy(m,st(:,t+1),1,res(:,t),1)
          call dgemv('n', m, m, alpha, tt(:,:,t_t), m, st(:,t), 1,
     + beta, res(:,t), 1)
      enddo
c$omp end do
c$omp end parallel

      end

c ----------------------------------------------------------------------

c  **/** NEW OPENMP HERE - UNTESTED **/**

c     subrouting calculates residuals from g_residual for time 
c     varying system matricies. Overwrites gt

      subroutine gres_res(res, gt, w, s, ifo, n, r, m, ng, lw, min_n_m)
      implicit none
      integer ifo,n,r,m,t,rank,info(n),ng,tg,timet
      integer lw, min_n_m      
      real*8 w(lw), s(min_n_m)    
      real*8 res(m,n-1), gt(m,r,ng)
      real*8 rcond
c ----------------------
cf2py intent(in) gres 
cf2py intent(inout) res 
cf2py intent(inout) ifo 
cf2py intent(in) gt
cf2py intent(in) w
cf2py intent(in) m
cf2py intent(in) r 
cf2py intent(in) n 
c ---------------------      
      rcond = -1.0
!     lw = 10 *m        

c$omp parallel default(shared) private(t, tg, rank, w, s)
c$omp do schedule(static)
      do t = 1, n-1      
          tg = timet(ng,t)
          call dgelss(m, r, 1, gt(:,:,tg), m, res(:,t), m, s, rcond,
     + rank, w, lw, info(t))                        
      enddo
c$omp end do
c$omp end parallel

c     Error checking:      
      t = 1
      ifo = 0
      do while ((t < n-1).and.(ifo.eq.0)) 
         if(info(t).ne.0) then
             ifo = 1
         endif
         t = t +1         
      enddo      
     
      end

c ----------------------------------------------------------------------

c     non-time varying verions of state_res
      subroutine ntstate_res(st,tt,res,n,m)
      implicit none
      integer n, m, t
      real*8 st(m,n), tt(m,m), res(m,n-1)
      real*8 alpha, beta
c ------------------
cf2py intent(in) st
cf2py intent(in) tt
cf2py intent(inout) res
cf2py intent(in) n
cf2py intent(in) m
c ------------------
      alpha = -1.0
      beta = 1.0
      
c$omp parallel default(shared) private(t)
c$omp do schedule(static)
      do t = 1, n-1
          call dcopy(m,st(:,t+1),1,res(:,t),1)
          call dgemv('n',m,m,alpha,tt,m,st(:,t),1,beta,
     + res(:,t),1)
      enddo
c$omp end do
c$omp end parallel
      end

c ---------------------------------------------------------------------

      subroutine eye(a,m)
      integer m, i, j
      real*8 a(m,m)

      do i = 1, m
          do j = 1, m
              a(i,j) = 0.0
          enddo
          a(i,i) = 1.0
      enddo
      end
        
c ----------------------------------------------------------------------        

c **/** NEW OPENMP ADDED - UNTESTED **/**

c     subroutine simulates statespace model with state  regressors
      subroutine srsimssm(y,zt,ch,wb,tt,cqt,rvm,rvs,av,r,n,p,m,
     + nz,nh,nt,nq)
      integer n,r,p,m,i,t
      integer nz,nh,nt,nq
      integer tz,th,t_t,tq,timet
      real*8 y(p,n), zt(p,m,nz), ch(p,1,nh), tt(m,m,nt), wb(m,n)
      real*8 rvm(p,n),rvs(r,n), av(m,n), cqt(m,r,nq)
      real*8 alpha, beta

c     cqt is the cholesky decomposition of qt
c     cht is the sqrt of the ht. recall that ht is a vector
C --------------------
cf2py intent(inout) y
cf2py intent(in) zt
cf2py intent(in) ch
cf2py intent(in) wb
cf2py intent(in) tt
cf2py intent(in) cqt
cf2py intent(in) rvm
cf2py intent(in) rvs
cf2py intent(inout) av
cf2py intent(in) n
cf2py intent(in) r
cf2py intent(in) p
cf2py intent(in) m
C -------------------
      alpha = 1.0        
 
c     Step 1.
c$omp parallel default(shared)
c$omp do schedule(static) private(t, tq, beta)   
      do t = 1, n-1                   
          tq = timet(nz,t)                             
c         Compute: av(t+1) = cqt(t) * rvs(t)              
          beta = 0.0
          call dgemv('n',m,r,alpha,cqt(:,:,tq),m,rvs(:,t),1,beta,
     + av(:,t+1),1)   
c         Compute: av(t+1) = av(t+1) + alpha * wb(t)     
          beta = 1.0
          call daxpy(m,alpha,wb(:,t),1,av(:,t+1),1) 
      enddo
c$omp end do
                       
c     Step 2.                       
c$omp single 
      beta = 1.0   
      do t = 1, n-1                              
          t_t = timet(nt,t)
c         Compute: av(t+1) = av(t+1) + tt(t) * av(t)        
          call dgemv('n',m,m,alpha,tt(:,:,t_t),m,av(:,t),1,beta,
     + av(:,t+1),1)     
      enddo
c$omp end single
           
c     Step 3. 
c$omp do schedule(static) private(t, tz, th, i)
      do t = 1, n      
          tz = timet(nz,t)
          th = timet(nh,t)          
          do i = 1, p
              y(i,t) = ch(i,1,th)*rvm(i,t)
          enddo
c         Compute: y(t) = y(t) + zt(t) * av(t)          
          call dgemv('n',p,m,alpha,zt(:,:,tz),p,av(:,t),1, beta,
     + y(:,t),1)
      enddo
c$omp end do
c$omp end parallel

      end

c ----------------------------------------------------------------------

c **/** NEW OPENMP ADDED - UNTESTED **/**

      subroutine simssm(y,zt,ch,tt,cqt,rvm,rvs,av,r,n,p,m,
     + nz,nt,nq,nh)    
    
      integer n,r,p,m, i, t
      integer tz, th, t_t, tq, nz, nh, nt, nq, timet
      real*8 y(p,n), zt(p,m,nz), ch(p,1,nh), tt(m,m,nt)
      real*8 rvm(p,n), rvs(r,n), av(m,n), cqt(m,r,nq)
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
cf2py intent(in) n
cf2py intent(in) r
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) nz
cf2py intent(in) nh
cf2py intent(in) nt
cf2py intent(in) nq
c --------------------

      alpha = 1.0
      beta = 0.0
      
c     Step 1.
c$omp parallel default(shared)
c$omp do schedule(static) private(t, tq)      
      do t = 1, n-1                    
          tq = timet(nq,t)
c         Compute: av(t+1) = cqt(t) * rvs(t)          
          call dgemv('n',m,r,alpha,cqt(:,:,tq),m,rvs(:,t),1,beta,
     + av(:,t+1),1)     
      enddo
c$omp end do      
 
c     Step 2.    
c$omp single    
      beta = 1.0
      do t = 1, n-1              
          t_t = timet(nt,t)
c         Compute: av(t+1) = av(t+1) + tt(t) * av(t)          
          call dgemv('n',m,m,alpha,tt(:,:,t_t),m,av(:,t),1,beta,
     + av(:,t+1),1)
      enddo
c$omp end single      

      beta = 1.0

c     Step 3. 
c$omp do schedule(static) private(t, i, th, tz)
      do t = 1, n
          th = timet(nh,t)          
          tz = timet(nz,t)
          do i = 1, p
              y(i,t) = ch(i,1,th) * rvm(i,t)
          enddo

c         Compute: y(t) = y(t) + zt(t) * av(t)          
          call dgemv('n',p,m,alpha,zt(:,:,tz),p,av(:,t),1, beta,
     + y(:,t),1)
      enddo
c$omp end do
c$omp end parallel

      end

c ----------------------------------------------------------------------

c **/** NEW OPENMP ADDED - UNTESTED **/**

c     non time varying version that simulates data with state regressors     
      subroutine ntsrsimssm(y,zt,ch,wb,tt,cqt,rvm,rvs,av,n,r,p,m)
      integer n,r,p,m, i, t
      real*8 y(p,n), zt(p,m), ch(p), tt(m,m), wb(m,n)
      real*8 rvm(p,n),rvs(r,n), av(m,n), cqt(m,r)
      real*8 alpha, beta

c     cqt is the cholesky decomposition of qt
c     cht is the sqrt of the ht. recall that ht is a vector
c ------------------------
cf2py intent(inout) y
cf2py intent(in) zt
cf2py intent(in) ch
cf2py intent(in) wb
cf2py intent(in) tt
cf2py intent(in) cqt
cf2py intent(in) rvm
cf2py intent(in) rvs
cf2py intent(inout) av
cf2py intent(in) n
cf2py intent(in) r
cf2py intent(in) p
cf2py intent(in) m
c -----------------------

      alpha = 1.0     

c$omp parallel default(shared)
c$omp do schedule(static) private(t, beta)
      do t = 1, n-1  

c         1a. Compute:  av(t+1) = cqt * rvs(t)     
          beta = 0.0        
          call dgemv('n',m,r,alpha,cqt,m,rvs(:,t),1,beta,
     + av(:,t+1),1)
         
c         1b. Compute: av(t+1) = av(t+1) + alpha * wb(t) 
          beta = 1.0
          call daxpy(m,alpha,wb(:,t),1,av(:,t+1),1)
      enddo
c$omp end do      

      beta = 1.0

c     Step 2. Compute: av(t+1) = av(t+1) + tt * av(t)
c$omp single
      do t = 1, n-1                    
          call dgemv('n',m,m,alpha,tt,m,av(:,t),1,beta,
     + av(:,t+1),1)
      enddo
c$omp end single      

c     Step 3.
      beta = 1.0
c$omp do schedule(static) private(t, i)
      do t = 1, n
          do i = 1, p
              y(i,t) = ch(i)*rvm(i,t)
          enddo
      enddo
c$omp end do
c$omp end parallel

c     Step 4. Compute: y = y + zt * av
      call dgemm('n','n',p,n,m,alpha,zt,p,av,m,beta,y,p)
      end

c ----------------------------------------------------------------------

c **/** NEW OPENMP ADDED - UNTESTED **/**

c     non time varying version that simulates data      
      subroutine ntsimssm(y,zt,ch,tt,cqt,rvm,rvs,av,n,r,p,m)
      integer n,r,p,m, i, t
      real*8 y(p,n), zt(p,m), ch(p), tt(m,m)
      real*8 rvm(p,n),rvs(r,n), av(m,n), cqt(m,r)
      real*8 alpha, beta

c     cqt is the cholesky decomposition of qt
c     cht is the sqrt of the ht. recall that ht is a vector
c -----------------------
cf2py intent(inout) y
cf2py intent(in) zt
cf2py intent(in) ch
cf2py intent(in) tt
cf2py intent(in) cqt
cf2py intent(in) rvm
cf2py intent(in) rvs
cf2py intent(inout) av
cf2py intent(in) n
cf2py intent(in) r
cf2py intent(in) p
cf2py intent(in) m
c -----------------------

      alpha = 1.0
      beta = 0.0
      
c     Step 1.  Compute: av(t+1) = cqt * rvs(t)      
c$omp parallel default(shared) 
c$omp do schedule(static) private(t)
      do t = 1, n-1              
          call dgemv('n',m,r,alpha,cqt,m,rvs(:,t),1,beta,
     + av(:,t+1),1)
      enddo
c$omp end do      
      
c     Step 2. Compute: av(t+1) = av(t+1) + tt * av(t)      
c$omp single     
      beta = 1.0
      do t = 1, n-1         
          call dgemv('n',m,m,alpha,tt,m,av(:,t),1,beta,
     + av(:,t+1),1)
      enddo
c$omp end single      
      
c     Step 3: Compute: y(i,t) = ch(i) * rvm(i,t) 
c$omp do schedule(static) private(t, i)
      do t = 1, n
          do i = 1, p
              y(i,t) = ch(i) * rvm(i,t)
          enddo
      enddo
c$omp end do
c$omp end parallel

c     Step 4. Compute: y = y + zt * av    [i.e.  (p,n) = (p,m) *(m,n)  ]
      beta = 1.0
      call dgemm('n','n',p,n,m,alpha,zt,p,av,m,beta,y,p)
      end
      
c ----------------------------------------------------------------------    
  
c     subroutines updates time varying matrix with non-time varying matrix
      subroutine updtv(tv,ntv,p,m,n)
      implicit none
      integer p,m,n,t,i
      real*8 tv(p,m,n), ntv(p,m)    
c ----------------------
cf2py intent(inout) tv
cf2py intent(in) tv
cf2py intent(in) m
cf2py intent(in) n
c ---------------------
c$omp parallel default(shared) private(t, i)
c$omp do schedule(static)
      do t = 1, n
          do i = 1, m
              call dcopy(p, ntv(:,i), 1, tv(:,i,t), 1)
          enddo
      enddo
c$omp end do
c$omp end parallel
      end
 
c ----------------------------------------------------------------------

c     for (A,i) subroutine returns returns (chol(A),i) for all i
      subroutine calc_chol(qt,info,r,n)
      implicit none
      integer r,n,t,i,j,info, infoc
      real*8 qt(r,r,n)
c -----------------------
cf2py intent(inout) qt
cf2py intent(inout) info
cf2py intent(in) r
cf2py intent(in) n
c -----------------------
c$omp parallel default(shared) private(t, i, j, infoc)
c$omp do schedule(static)
      do t = 1, n
          call dpotrf('l', r,qt(:,:,t),r,infoc)
          do i = 1, r
              do j = i+1, r
                  qt(i,j,t) = 0.0
              enddo
          enddo
              
          if (infoc.ne.0) then
              info = 1
          endif
      enddo
c$omp end do
c$omp end parallel
      end

c ----------------------------------------------------------------------

c     subroutine used in state space transform unifilter
      subroutine transform_u(ch,zt,p,n,m,nz)
      implicit none
      integer p,n,m,t,nz,tz,timet
      real*8 ch(p,p), zt(p,m,nz), alpha
c -----------------------    
cf2py intent(in) ch
cf2py intent(inout) zt
cf2py intent(in) p
cf2py intent(in) n
cf2py intent(in) 
c -----------------------
      alpha = 1.0
c$omp parallel default(shared) private(t, tz)
c$omp do schedule(static)
      do t = 1, n
          tz = timet(nz,t)
          call dtrmm('l','u','n','n',p,m,alpha,ch,p,zt(:,:,tz),p)
      enddo
c$omp end do
c$omp end parallel
      end
    
c ----------------------------------------------------------------------
    
c     function returns correct t for use in time varying case
      integer function timet(n,t)
      implicit none
      integer n,t

      timet = 1
      if (n.gt.1) then
          timet = t
      endif
      return
      end function timet

c ----------------------------------------------------------------------

c     subroutine used to update qtcqt
      subroutine update_gtcqt(gtcqt,gt,cqt,m,r,ng,nq,n)
      implicit none
      integer m,r,ng,nq,t,tg,tq,n
      integer timet
      real*8 gt(m,r,ng), cqt(r,r,nq), gtcqt(m,r,n)
      real*8 alpha, beta
c ---------------------------
cf2py intent(inout) gtcqt
cf2py intent(in) gt
cf2py intent(in) cqt
cf2py intent(in) m
cf2py intent(in) r
cf2py intent(in) ng
cf2py intent(in) nq
c -------------------
      alpha = 1.0
      beta = 0.0
c$omp parallel default(shared) private(t, tg, tq) 
c$omp do schedule(static)
      do t = 1, n
          tg = timet(ng,t)
          tq = timet(nq,t)
          call dgemm('n','n',m,r,r,alpha,gt(:,:,tg),m,cqt(:,:,tq),r,
     + beta,gtcqt(:,:,t),m)
      enddo
c$omp end do
c$omp end parallel
      end

c ----------------------------------------------------------------------

c     subroutine used to update gqg'
      subroutine update_gqg(gqg,qt,gqt,gt,m,r,ng,nq,n)
      implicit none
      integer timet
      integer m,r,n,t,ng,nq,tg,tq
      real*8 gqg(m,m,n),qt(r,r,nq),gt(m,r,ng),gqt(m,r)
      real*8 alpha, beta
c ----------------------
cf2py intent(inout) gqg
cf2py intent(in) gcqt
cf2py intent(in) gt
cf2py intent(in) m
cf2py intent(in) r
cf2py intent(in) ng
cf2py intent(in) nq
c --------------------
      alpha = 1.0
      beta = 0.0

c$omp parallel default(shared) private(t, tg, tq, gqt)
c$omp do schedule(static)
      do t = 1, n
          tg = timet(ng,t)
          tq = timet(nq,t)          
c         Compute: gqt = gt(t) * qt(t)          
          call dgemm('n','n',m,r,r,alpha,gt(:,:,tg),m,qt(:,:,tq),r,beta,
     + gqt(:,:),m)
c         Compute: gqg(t) =  gqt * gt*t)    
          call dgemm('n','t',m,m,r,alpha,gqt,m,gt(:,:,tg),m,beta,
     + gqg(:,:,t),m)
      enddo
c$omp end do
c$omp end parallel
      end

c ----------------------------------------------------------------------

c     subroutine that calculates ztilde = z(t).*(kron(state(t)'ones(p)))
      subroutine calc_ztilde(zt,st,ztil,p,m,n)
      implicit none
      integer p,m,n,t,i
      real*8 zt(p,m,n),st(m,n),ztil(p,m,n)

c$omp parallel default(shared) private(t, i)
c$omp do schedule(static)
      do t = 1, n
          do i = 1, m
              call dcopy(p, zt(:,i,t), 1, ztil(:,i,t), 1)
              call dscal(p, st(i,t), ztil(:,i,t), 1)
          enddo
      enddo
c$omp end do
c$omp end parallel
 
      end

c     non - timvaring verion of the univariate filtering algorithm      
c     with regressors
      subroutine ntunifilter_r(y,nf,k,at,pt,a,pm,z,h,mt,tt,q,pttt,
     + lk,ilike,wb,p,m,n)
      implicit none
      integer p,m,n,i,t,j,ilike
      real*8 y(p,n), nf(p,n,2), k(m,p,n), at(m,n), pt(m,m,n)
      real*8 q(m,m), mt(m,p), tt(m,m), h(p), pttt(m,m), z(p,m)
      real*8 a(m), pm(m,m),lk(*),llike,wb(m,n)
      real*8 ddot, alpha, beta,as


c     y - (p*n) is a matrix containing the dependent variable
c     nf - (p*n*2) nf(:,1) is nustore, nf(:,2) is fstore
c     ka - (m,p+1,n,2) ka(:,:,1)= kstore, ka(:,:,2) is astore
c     pt - (m,m,p+1,n) 
c     z - (m,p,n) is the system matrix Zt
c     h - (p*n) is the system matrix Ht. Note that Ht is diagonal
c     q - (m*m*n) is the system matrix r, q=GQG'
c     w - (m,m) is a work array.
c -----------------------
cf2py intent(in) y
cf2py intent(inout) nf
cf2py intent(inout) k
cf2py intent(inout) at
cf2py intent(inout) pt
cf2py intent(in) a
cf2py intent(in) pm
cf2py intent(in) z
cf2py intent(in) h
cf2py intent(in) mt
cf2py intent(in) tt
cf2py intent(in) pttt
cf2py intent(inout) lt
cf2py intent(inout) lk
cf2py intent(in) wb
cf2py intent(in) q
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
c -----------------------
      llike=0.0
      do t=1,n
          call dcopy(m,a,1,at(:,t),1)
          do j=1,m
              call dcopy(m,pm(:,j),1,pt(:,j,t),1) 
          enddo
          do i=1,p
              alpha=1.0
              beta=0.0

c                 Compute: nu(t,i) = y(t,i) - z(t,i)'a(t,i)
              nf(i,t,1)=y(i,t)-ddot(m,z(i,:),1,a,1)

c                 Compute: m(t,i) = P(t,i) * z(t,i)
              call dgemv('n',m,m,alpha,pm,m,z(i,:),1,beta,mt(:,i),1)

c                 Compute: f(t,i) = z(t,i)'m(t,i) + 1
              nf(i,t,2)=ddot(m,z(i,:),1,mt(:,i),1)+h(i)
              
              do j = 1, m

c                     Compute: k(t,i) = m(t,i) / f(t,i)
                  k(j,i,t)=mt(j,i)/nf(i,t,2)

c                     Compute: a(t,i+1) = a(t,i) + k(t,i) * nu(t,i)
                  as=a(j)+k(j,i,t)*nf(i,t,1)
                  a(j)=as
              enddo
              
              alpha=-1.0

c                 Compute: P(t,i+1) = P(t,i) - k(t,i) * m(t,i)'
              call dger(m,m,alpha,k(:,i,t),1,mt(:,i),1,pm,m)
              if (ilike.eq.0) then
                  llike=llike-0.5*(log(nf(i,t,2))+nf(i,t,1)*
     + nf(i,t,1)/nf(i,t,2))
              endif
          enddo
          alpha=1.0
          
c             Compute: a(t+1,1) = W(t) * beta+ T(t) * a(t,p+1)
          call dgemv('n',m,m,alpha,tt,m,a,1,beta,pttt(:,1),1)
          call dcopy(m,pttt(:,1),1,a,1)
          !modification for regressors
          call daxpy(m,alpha,wb(:,t),1,a,1)
          alpha=1.0
          beta=0.0
          
c             Compute: P(t+1,i) = T(t) * P(t,p+1)T(t)' + G(t)*inv(Q)*G(t)'
          call dgemm('n','t',m,m,m,alpha,pm,m,tt,m,beta, pttt,m)
          do i=1,m
              call dcopy(m,q(:,i),1,pm(:,i),1)
          enddo
          beta=1.0
          call dgemm('n','n',m,m,m,alpha,tt,m,pttt,m,beta,pm,m) 
      enddo
      lk(1)=llike
      end

c ----------------------------------------------------------------------
c ----------------------------------------------------------------------
c     fortran code for univariate filtering algorithms with regressors
c ----------------------------------------------------------------------
      
       subroutine unifilter_r(y, nf, k, at, pt, a, pm, z, h, mt, tt, q,
     + pttt, lk, ptt, ilike, wb, p, m, n, nz, nh, nt, nq)     
     
      implicit none
      integer p,m,n,ptt,i,t,j,ilike
      integer tz,th,t_t,tq,timet
      integer nz, nh, nt, nq
      real*8 y(p,n), nf(p,n,2), k(m,p,n), at(m,n), pt(m,m,n)
      real*8 q(m,m,nq), mt(m), tt(m,m,nt), h(p,1,nh), pttt(m,m)
      real*8 a(m), pm(m,m), lk(*),llike, z(p,m,nz), wb(m,n)
      real*8 ddot, alpha, beta,as


c     y - (p*n) is a matrix containing the dependent variable
c     nf - (p*n*2) nf(:,1) is nustore, nf(:,2) is fstore
c     ka - (m,p+1,n,2) ka(:,:,1)= kstore, ka(:,:,2) is astore
c     pt - (m,m,p+1,n) 
c     z - (m,p,n) is the system matrix Zt
c     h - (p*n) is the system matrix Ht. Note that Ht is diagonal
c     q - (m*m*n) is the system matrix r, q=GQG'
c     w - (m,m) is a work array.
c ----------------------
cf2py intent(in) y
cf2py intent(inout) nf
cf2py intent(inout) k
cf2py intent(inout) at
cf2py intent(inout) pt
cf2py intent(in) a
cf2py intent(in) pm
cf2py intent(in) z
cf2py intent(in) h
cf2py intent(in) mt
cf2py intent(in) tt
cf2py intent(in) pttt
cf2py intent(in) ptt
cf2py intent(inout) lk
cf2py intent(in) wb
cf2py intent(in) q
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) nz
cf2py intent(in) nh
cf2py intent(in) nt
cf2py intent(in) nq
c ---------------------
      llike = 0.0
              
      do t = 1, n
      
          tz = timet(nz,t)
          th = timet(nh,t)
          t_t = timet(nt,t)          
          tq = timet(nq,t)

          call dcopy(m,a,1,at(:,t),1)
          do j = 1, m
              call dcopy(m, pm(:,j),1, pt(:,j,t),1) 
          enddo
          
          do i = 1, p

              alpha = 1.0
              beta = 0.0
              if (isnan(y(i,t)).eqv..FALSE.) then
                  nf(i,t,1) = y(i,t) - ddot(m,z(i,:,tz),1,a,1)
                  
                  call dgemv('n',m,m,alpha,pm,m,z(i,:,tz),1,beta,mt,
     + 1)
                  
                  nf(i,t,2) = ddot(m,z(i,:,tz),1,mt,1) + h(i,1,th)
                  do j = 1, m
                      k(j,i,t) = mt(j) / nf(i,t,2)
                      as = a(j) + k(j,i,t)*nf(i,t,1)
                      a(j) = as
                  enddo
                  alpha = -1.0
                  call dger(m,m,alpha,k(:,i,t),1, mt,1, pm,m)
                  if (ilike.eq.0) then
                      llike = llike - 0.5*(log(nf(i,t,2))+nf(i,t,1)**2 /
     + nf(i,t,2))
                  endif
              endif
          enddo
          alpha = 1.0
          if (ptt.eq.0) then
              call dgemv('n',m,m,alpha,tt(:,:,t_t),m,a,1,beta,
     + pttt(:,1),1)
              call dcopy(m,pttt(:,1),1,a,1)
          endif
          !modification for regressors
          call daxpy(m,alpha,wb(:,t),1,a,1)
          
          if (ptt.eq.0) then
              alpha = 1.0
              beta = 0.0
              call dgemm('n','t',m,m,m,alpha,pm,m,tt(:,:,t_t),m,beta,
     +  pttt,m)
              do i = 1, m
                  call dcopy(m, q(:,i,tq),1, pm(:,i),1)
              enddo
              beta = 1.0
              call dgemm('n','n',m,m,m,alpha, tt(:,:,t_t),m,pttt,m,beta,
     + pm,m) 
          else
              do j = 1, m
                  call daxpy(m,alpha, q(:,j,tq),1, pm(:,j),1)
              enddo
          endif
      enddo
      lk(1)=llike
      end
      

c ----------------------------------------------------------------------

c     subroutine that calculates ztilde = z(t).*(kron(state(t)'ones(p)))
c     non-timevarying system matrices
      subroutine ntcalc_ztilde(zt,st,ztil,p,m,n)
      implicit none
      integer p,m,n,t,i
      real*8 zt(p,m),st(m,n),ztil(p,m,n)
  
c$omp parallel default(shared) private(t, i)
c$omp do schedule(static)
      do t = 1, n
          do i = 1, m
              call dcopy(p, zt(:,i),1, ztil(:,i,t),1)
              call dscal(p, st(i,t), ztil(:,i,t),1)
          enddo
      enddo
c$omp end do
c$omp end parallel
      end

c ----------------------------------------------------------------------

c     subroutine that calculates ystar = y + zt(:,i) for all t
      subroutine calc_ystar(res,ys,z,xs,i,p,n,m,nz)
      implicit none
      integer p,n,m,i,t,j,k
      integer nz,tz,timet
      real*8 res(p,n),ys(p*n),z(p,m,nz),xs(p*n)
      real*8 alpha
c -----------------------
cf2py intent(in) res      
cf2py intent(inout) ys
cf2py intent(in) z     
cf2py intent(inout) xs  
cf2py intent(in) i      
cf2py intent(in) p      
cf2py intent(in) m      
cf2py intent(in) n      
c -----------------------
      alpha = 1.0      
              
c$omp parallel default(shared) private(t, tz, j, k)
c$omp do schedule(static)
      do t = 1, n
          tz = timet(nz,t)
          do j = 1, p
              k = (t-1) * p + j
              ys(k) = res(j,t) + z(j,i,tz)
              xs(k) = z(j,i,tz)              
          enddo
      enddo
c$omp end do
c$omp end parallel

      end

c ----------------------------------------------------------------------

c     subroutine that scales the columns of Z with a vector
      subroutine scale_z(zt,sc,p,m)
      implicit none
      integer p,m,i
      real*8 zt(p,m), sc(m)
c -----------------------
cf2py intent(inout) zt
cf2py intent(in) sc
cf2py intent(in) p
cf2py intent(in) m
c -----------------------    
c$omp parallel default(shared) private(i)
c$omp do schedule(static)
      do i = 1, m
          call dscal(p, sc(i), zt(:,i), 1)
      enddo
c$omp end do
c$omp end parallel
      end

c ----------------------------------------------------------------------

c     subroutine that scales the columns of Z with a vector
c     for the time varying case
      subroutine scale_ztv(zt,sc,p,m,n)
      implicit none
      integer p,m,n,i,t
      real*8 zt(p,m,n), sc(m)
c -----------------------
cf2py intent(inout) zt
cf2py intent(in) sc
cf2py intent(in) p
cf2py intent(in) m
cf2py intent(in) n
c -----------------------
      
c$omp parallel default(shared) private(t, i)
c$omp do schedule(static)
      do t = 1, n
          do i = 1, m
              call dscal(p, sc(i), zt(:,i,t), 1)
          enddo
      enddo
c$omp end do
c$omp end parallel
      end

c ----------------------------------------------------------------------          
        
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

c ----------------------------------------------------------------------

c     subroutine calculates the Frobenius norm for the difference of two matrices
c     passed as a vector. Only the minimu of n and 6 elements are used
c     in the calculation of the norm
      real*8 function fnormv(a,b,n)
      implicit none
      integer m,n,i
      real*8 a(n),b(n), sumd

      if (n.gt.6) then
          m=6
      else
          m=n
      endif
      sumd=0.0

      do i=1,m
          sumd=sumd+(a(i)-b(i))**2
      enddo
      fnormv=sqrt(sumd)
      return
      end
      
c ----------------------------------------------------------------------

      subroutine printm(a,m,n)
      implicit none
      integer m,n,i,j
      real*8 a(m,n)

      do i=1,m
          write(*,*) (a(i,j),j=1,m)
      enddo
      end
      
c ----------------------------------------------------------------------
