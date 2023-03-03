## Filtering RSSI with Kalman Filter
<b>500 continuous records of iBeacon signal.</b>
<p>Producing white noise to compare with our data.</p>

![white_noise_check](./white_noise_check.png)

<p>Plot data's density & random gaussian's density, they are same shape.</p>

![gauss_check](./gaussian_check.png)

<p>We can treat our sensor signal as a Gaussian, it's error is about <b>3.84(dBm)</b>.</p>

## Filtered result
<p>Data has been collected while standing.</p>

![plot](./kf_smooth.png)

