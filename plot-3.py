import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from model import model

d4a=np.loadtxt("data/results_rscaletest-gke4_nodybat.txt")
d4b=np.loadtxt("data/results_rscaletest-gke4_nodybat_bigbat.txt")

# EMTrackMichelID Time
fig=plt.figure()
ax=fig.add_subplot(111)

ax.set_xlim(0,500)
ax.set_ylim(0,250)
ax.grid(True)
ax.errorbar(d4a[:,0], d4a[:,3], yerr=d4a[:,4]/np.sqrt(d4a[:,0]), fmt='r^--', linewidth=0.8,markersize=7, markeredgecolor='red', fillstyle='none', capsize=3, label = "w/ Triton on GKE-4gpu, avg batch size = 235")
ax.errorbar(d4b[:,0], d4b[:,3], yerr=d4b[:,4]/np.sqrt(d4b[:,0]), fmt='bD--', linewidth=0.8,markersize=5.5, markeredgecolor='blue', fillstyle='none', capsize=3, label = "w/ Triton on GKE-4gpu, avg batch size = 1700")
ax.set(title="EmTrkMichelId module proc time vs # jobs (GKE-4gpu, no dynamic batching)", xlabel="number of simultaneous jobs", ylabel="processing time [seconds]")

#xr=[0.,310.]
#yr=[219.4,219.4]
#ax.plot(xr, yr, color='orange',label = "without Triton",linestyle='solid',linewidth=2)

xm = np.arange(0.,500.)
ym = model(xm, False, False, True)
ax.plot(xm, ym, color='purple',label = "model (small batch)",linestyle='dotted',linewidth=2)

xm = np.arange(0.,500.)
ym = model(xm,False,True, True)
ax.plot(xm, ym, color='cyan',label = "model (big batch)",linestyle='dotted',linewidth=2)

xr=[0.,500.]
yr=[220,220]
ax.plot(xr, yr, color='orange',label = "CPU-only (w/o Triton)",linestyle='solid',linewidth=2)

ax.legend()
fig.tight_layout()
fig.savefig("plot-3_EMTrackMichelID.pdf")
fig.savefig("plot-3_EMTrackMichelID.png")
fig.show()

# Full Event Time
fig2=plt.figure()
ax2=fig2.add_subplot(111)

ax2.set_xlim(0,500)
ax2.set_ylim(0,350)
ax2.grid(True)
ax2.errorbar(d4a[:,0], d4a[:,1], yerr=d4a[:,2]/np.sqrt(d4a[:,0]), fmt='r^--', linewidth=0.8,markersize=7, markeredgecolor='red', fillstyle='none', capsize=3, label = "w/ Triton on GKE-4gpu, avg batch size = 235")
ax2.errorbar(d4b[:,0], d4b[:,1], yerr=d4b[:,2]/np.sqrt(d4b[:,0]), fmt='bD--', linewidth=0.8,markersize=5.5, markeredgecolor='blue', fillstyle='none', capsize=3, label = "w/ Triton on GKE-4gpu, avg batch size = 1700")
ax2.set(title="Full Event proc time vs # jobs (GKE-4gpu, no dynamic batching)", xlabel="number of simultaneous jobs", ylabel="processing time [seconds]")

xm = np.arange(0.,500.)
ym = model(xm)
ax2.plot(xm, ym, color='purple',label = "model(small batch)",linestyle='dotted',linewidth=2)

xm = np.arange(0.,500.)
ym = model(xm,False,True)
ax2.plot(xm, ym, color='cyan',label = "model (big batch)",linestyle='dotted',linewidth=2)

xr=[0.,500.]
yr=[330,330]
ax2.plot(xr, yr, color='orange',label = "CPU-only (w/o Triton)",linestyle='solid',linewidth=2)

ax2.legend()
fig2.tight_layout()
fig2.savefig("plot-3_FullEvent.pdf")
fig2.savefig("plot-3_FullEvent.png")
fig2.show()