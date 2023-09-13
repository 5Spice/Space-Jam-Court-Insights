import { ChangeDetectorRef, Component, OnDestroy, OnInit, ViewEncapsulation } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { untilDestroyed, UntilDestroy } from '@ngneat/until-destroy';
import { PlayersService } from '../_services/players.service';
import { HttpClient } from '@angular/common/http'; // Import HttpClient
import { PlayerSummary } from './player-summary.interface'; // Import the PlayerSummary interface

@UntilDestroy()
@Component({
  selector: 'player-summary-component',
  templateUrl: './player-summary.component.html',
  styleUrls: ['./player-summary.component.scss'],
  encapsulation: ViewEncapsulation.None,
})
export class PlayerSummaryComponent implements OnInit, OnDestroy {
  isLoading: boolean = true;
  error: string | null = null;

  playerSummary: PlayerSummary = {
    name: 'N/A',
    points: 'N/A',
    assists: 'N/A',
    rebounds: 'N/A',
    minutesPlayed: 'N/A',
    defensiveFouls: 'N/A',
    offensiveFouls: 'N/A',
    freeThrowsMade: 'N/A',
    freeThrowsAttempted: 'N/A',
    twoPointersMade: 'N/A',
    twoPointersAttempted: 'N/A',
    threePointersMade: 'N/A',
    threePointersAttempted: 'N/A',
  };

  constructor(
    protected activatedRoute: ActivatedRoute,
    protected cdr: ChangeDetectorRef,
    protected playersService: PlayersService,
    private http: HttpClient // Inject HttpClient
  ) {}

  ngOnInit(): void {
    this.activatedRoute.params.pipe(untilDestroyed(this)).subscribe((params) => {
      const playerId = params.playerID; // Get player ID from the route parameter
      const apiUrl = `http://localhost:8000/api/v1/playerSummary/${playerId}`;

      this.http.get(apiUrl).pipe(untilDestroyed(this)).subscribe(
        (data: PlayerSummary) => {
          this.isLoading = false;
          this.playerSummary = data;

          // Set the shot points based on the provided shot data
          this.setShotPoints(data.shots);
        },
        (error) => {
          this.isLoading = false;
          this.error = 'Failed to load player summary data.';
        }
      );
    });
  }

  setShotPoints(shotData: any[]): void {
    // Assuming shotData is an array of shot objects with properties: isMake, locationX, and locationY
    shotData.forEach((shot) => {
      const shotPoint = document.createElement('div');
      shotPoint.className = 'shot-point';
      shotPoint.style.setProperty('--locationX', `${shot.locationX}ft`);
      shotPoint.style.setProperty('--locationY', `${shot.locationY}ft`);

      // Append the shot point to the shot chart container
      document.querySelector('.shot-chart-container')?.appendChild(shotPoint);
    });
  }

  ngOnDestroy() {}
}
