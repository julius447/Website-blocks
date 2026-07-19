<?php
/**
 * Ampy — Hero 1 "Elinstallationer i hemmet, gjort ordentligt." (startsidans section 1)
 * FluentSnippets: lägg som PHP-snippet (Run everywhere). Ger shortcoden:
 *
 *     [ampy_hero1]
 *
 * - Markup 1:1 från den ägargodkända prototypen (julius447.github.io/Hero-1).
 * - CSS ligger i den separata CSS-snippeten (hero-1.css) — denna fil skriver
 *    INGEN CSS. Ingen JS behövs (blocket är helt statiskt).
 * - ACF-fält (valfria — faller tillbaka på den godkända copyn om de saknas):
 *       hero_heading                → H1
 *       hero_text                   → lead-paragrafen
 *       google_rating               → "5,0"
 *       google_business_profile_url → länkmål för trust-raden
 * - Bakgrundsbilden: ladda upp assets/hero-1-bg.webp till mediabiblioteket och
 *   uppdatera AMPY_HERO1_IMG nedan om filnamnet blir ett annat.
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }

const AMPY_HERO1_IMG = '/wp-content/uploads/hero-1-bg.webp';

add_shortcode( 'ampy_hero1', function () {

	$heading = function_exists( 'get_field' ) ? get_field( 'hero_heading' ) : '';
	$lead    = function_exists( 'get_field' ) ? get_field( 'hero_text' ) : '';
	$rating  = function_exists( 'get_field' ) ? get_field( 'google_rating' ) : '';
	$gurl    = function_exists( 'get_field' ) ? get_field( 'google_business_profile_url' ) : '';

	// Rubriken är LÅST och innehåller ett medvetet <br> (2-radig desktop, döljs på mobil via CSS).
	$heading = $heading ? $heading : 'Elinstallationer i hemmet,<br> gjort ordentligt.';
	$lead    = $lead ? $lead : 'Våra egna behöriga elektriker hjälper dig i hela Sverige, med allt från elfel och elcentraler till laddbox och batterilagring.';
	$rating  = $rating ? $rating : '5,0';
	// Google-recensioner (owner-confirmed Maps-URL 2026-07-19).
	$gurl    = $gurl ? $gurl : 'https://www.google.com/maps/place/Ampy/@59.3576299,17.9842061,17z/data=!3m1!4b1!4m6!3m5!1s0x2bec1ce5c4ed9ce9:0xfce1752e84a1bfee!8m2!3d59.3576272!4d17.986781!16s%2Fg%2F11ypjy9rrm';

	$star = '<svg viewBox="0 0 24 24"><path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.9L12 17.8 5.8 21l1.2-6.9-5-4.9 6.9-1z"/></svg>';

	ob_start();
	?>
<section class="ampy-hero1" aria-label="Ampy – el i hemmet">
  <div class="ampy-hero1__frame">
    <img src="<?php echo esc_url( AMPY_HERO1_IMG ); ?>" alt="Upplyst villa i skymningen med el installerad av Ampy" fetchpriority="high" loading="eager">
    <div class="ampy-hero1__veil" aria-hidden="true"></div>
    <div class="ampy-hero1__content">
      <h1 class="ampy-hero1__title"><?php echo wp_kses( $heading, array( 'br' => array() ) ); ?></h1>
      <p class="ampy-hero1__lead"><?php echo esc_html( $lead ); ?></p>
      <a class="ampy-hero1__cta" href="<?php echo esc_url( home_url( '/kontakt/' ) ); ?>">
        Kostnadsfri rådgivning
        <svg class="pil" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4.7 11.3 11.3 4.7M11.3 4.7H4.7M11.3 4.7v6.6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
    </div>
    <div class="ampy-hero1__proof">
      <a class="g-row" href="<?php echo esc_url( $gurl ); ?>" target="_blank" rel="noopener" aria-label="Ampys omdömen, <?php echo esc_attr( $rating ); ?> på Google">
        <svg class="g-icon" width="16" height="16" viewBox="0 0 48 48" aria-hidden="true"><path fill="#FFC107" d="M43.6 20.1H42V20H24v8h11.3C33.7 32.7 29.2 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3.1 0 5.9 1.2 8 3l5.7-5.7C34.2 6.1 29.3 4 24 4 13 4 4 13 4 24s9 20 20 20 20-9 20-20c0-1.3-.1-2.6-.4-3.9z"/><path fill="#FF3D00" d="m6.3 14.7 6.6 4.8C14.7 15.1 19 12 24 12c3.1 0 5.9 1.2 8 3l5.7-5.7C34.2 6.1 29.3 4 24 4 16.3 4 9.7 8.3 6.3 14.7z"/><path fill="#4CAF50" d="M24 44c5.2 0 9.9-2 13.4-5.2l-6.2-5.2C29.2 35.1 26.7 36 24 36c-5.2 0-9.6-3.3-11.3-8l-6.5 5C9.5 39.6 16.2 44 24 44z"/><path fill="#1976D2" d="M43.6 20.1H42V20H24v8h11.3c-.8 2.2-2.2 4.2-4.1 5.6l6.2 5.2C41.4 34.8 44 29.9 44 24c0-1.3-.1-2.6-.4-3.9z"/></svg>
        <span class="g-label"><strong><?php echo esc_html( $rating ); ?></strong> på Google</span>
        <span class="stars" aria-hidden="true"><?php echo str_repeat( $star, 5 ); // phpcs:ignore WordPress.Security.EscapeOutput -- statisk SVG-konstant ?></span>
      </a>
      <span class="sep" aria-hidden="true"></span>
      <span class="vol">Över <strong>3 000</strong> installationer per år</span>
    </div>
  </div>
</section>
	<?php
	return ob_get_clean();
} );
