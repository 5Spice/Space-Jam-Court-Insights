import { ChangeDetectorRef, Component, OnDestroy, OnInit, ViewEncapsulation } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { untilDestroyed, UntilDestroy } from '@ngneat/until-destroy';
import { PlayersService } from '../_services/players.service';
import { HttpClient } from '@angular/common/http'; // Import HttpClient

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

  playerSummary: any = {
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
    const playerId = 1; // Replace with the player ID you want to fetch
    const apiUrl = `http://localhost:8000/api/v1/playerSummary/${playerId}`; 

    this.http.get(apiUrl).pipe(untilDestroyed(this)).subscribe(
      (data: any) => {
        this.isLoading = false;
        this.playerSummary = data.apiResponse;
      },
      (error) => {
        this.isLoading = false;
        this.error = 'Failed to load player summary data.';
      }
    );
  }

  ngOnDestroy() {}
}
