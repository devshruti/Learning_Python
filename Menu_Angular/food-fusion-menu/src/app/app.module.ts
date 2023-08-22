import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './components/app.component';
import { FlexLayoutModule } from '@angular/flex-layout';
import { MenuComponent } from './components/menu/menu.component'; // Import statement
import { HttpClientModule } from '@angular/common/http';
import { RouterModule, Routes } from '@angular/router';
// import { AboutComponent } from './about/about.component';


const routes: Routes = [
  { path: '', component: MenuComponent }, // Default route
  // { path: 'about', component: AboutComponent }, // Add this route
];

@NgModule({
  declarations: [
    AppComponent,
    MenuComponent
  ],
  imports: [
    BrowserModule,
    FlexLayoutModule,
    HttpClientModule,
    AppRoutingModule,
    RouterModule.forRoot(routes),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
